from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book
from comments.models import Comment
from .forms import BookCreateForm
from comments.forms import CommentCreateForm

from django.contrib.auth.models import User

# Create your views here.

app_name='stories'
def index(request):
    object_list = Book.objects.filter(draft=False)
    object_list_2 = Book.objects.filter(draft=True)
    objects_list_comments = Comment.objects.all()[:15]
    paginator = Paginator(object_list, 7)

    all_books = Book.objects.all()

    tot_readings = 0
    for book in all_books:
        tot_readings += book.readings

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    context = {'object_list': object_list,
                'object_list_2':object_list_2,
                'all_books':all_books,
                'tot_readings':tot_readings,
                'objects_list_comments':objects_list_comments,
                 }


    return render(request, 'stories/index.html', context )


def my_page(request):
     user = request.user
     object_list = Book.objects.filter(author=user)
     tot_readings = 0
     for obj in object_list:
        tot_readings += obj.readings

     return render(request, 'stories/my_page.html', {'object_list': object_list, 'tot_readings':tot_readings})


def detail_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    summary = book.book_summarys()
    submit = 'Kast'
    form = CommentCreateForm(request.POST or None)
    try:
        if Comment.objects.get(comment_writer=request.user, book=book):
            comment = Comment.objects.get(comment_writer=request.user, book=book)
            form = CommentCreateForm(request.POST or None, instance=comment)
    except:
        pass





    if form.is_valid():
        user_logged_in = request.user
        comment = form.save(commit=False)
        comment.comment_writer = user_logged_in

        dice = form.cleaned_data.get('dice')
        comment.dice = dice

        comment.book = book

        comment.save()

        return redirect("/")


    context = {
        'book': book,
        'summary': summary,
        'form':form,
        'submit':submit
    }

    return render(request, 'stories/detail_book.html', context)


def read_book(request, book_id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    book = get_object_or_404(Book, pk=book_id)

    author = book.author
    if author != request.user:
        readings = book.readings
        readings += 1
        book.readings = readings
        book.save()

    object_list = book.story.splitlines()
    paginator = Paginator(object_list, 11)

    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)

    return render(request, 'stories/read_book.html', {'book':book, 'object_list':object_list})


def detail_author(request, author_id):
    author = get_object_or_404(User, pk=author_id)
    books = Book.objects.filter(author=author_id, draft=False).order_by('published')
    tot_readings = 0
    for book in books:
        tot_readings += book.readings


    context = {
        'author':author,
        'books':books,
        'tot_readings':tot_readings,
        }

    return render(request, 'stories/detail_author.html', context)


def favorite_book_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author_id)
    try:
        selected_book = author.book_set.get(pk=request.POST['book'])
    except (KeyError, Book.DoesNotExist):
        return render(request, 'stories/detail_author.html', {
            'author':author, 'books':books,
            'error_message': 'Prove igjen: Du ma velge en favoritt-bok forst'
        })
    else:
        if selected_book.is_favorite:
            selected_book.is_favorite = False
        else:
            selected_book.is_favorite = True
        selected_book.save()
        return render(request, 'stories/detail_author.html', {'author': author, 'books': books})


def create_book(request):
    title = 'Lag ny bok'
    form = BookCreateForm(request.POST or None)
    user = request.user
    
    if not user.is_authenticated:
        return redirect('/')
    

    if form.is_valid():
        user_logged_in = request.user
        book = form.save(commit=False)
        author = user_logged_in
        book.author = author

        title = form.cleaned_data.get('title')
        book.first_name = title
        
        draft = form.cleaned_data.get('draft')
        book.draft = draft

        genre = form.cleaned_data.get('genre')
        book.genre = genre

        cover_picture = form.cleaned_data.get('cover_picture')

        if len(cover_picture) > 2:
            book.cover_picture = cover_picture

        else:
            book.cover_picture = 'http://www.mcsenteret.com/images/manglerbilde.jpg'

        story = form.cleaned_data.get('story')
        book.story = story

        book.save()

        return redirect("stories:my_page")

    context = {
        'form': form,
        'title': title,
    }

    return render(request, "form.html", context)

def edit_book(request, id=None):
    title = 'Oppdater bok'
    book = Book.objects.get(id=id)
    form = BookCreateForm(request.POST or None, instance=book)
    user = request.user
    author = book.author
    print(author.id, user.id)

    if author.id != user.id:
        return redirect('/')

    if form.is_valid():
        user_logged_in = request.user
        book = form.save(commit=False)

        title = form.cleaned_data.get('title')
        book.first_name = title

        genre = form.cleaned_data.get('genre')
        book.genre = genre

        draft = form.cleaned_data.get('draft')
        book.draft = draft

        cover_picture = form.cleaned_data.get('cover_picture')
        book.cover_picture = cover_picture

        story = form.cleaned_data.get('story')
        book.story = story

        book.save()

        return redirect('stories:read_book', book.id)

    context = {
        'title':title,
        'form':form,
        'book':book,

    }
    return render(request, "form.html", context)

def delete_book(request, id=None):
    book = Book.objects.get(id=id)
    user = request.user
    author = book.author

    if author.id != user.id:
        return redirect('/')

    book.delete()

    return redirect('stories:my_page')