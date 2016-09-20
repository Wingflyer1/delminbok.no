from django.shortcuts import render, redirect
from .models import Comment



# Create your views here.

def index(request):

    if not request.user.is_staff:
        return redirect('/')

    user = request.user
    object_list_comments = Comment.objects.all()

    context = {
        'user': user,
        'object_list_comments':object_list_comments,
    }
    return render(request, "comments/index.html", context)



