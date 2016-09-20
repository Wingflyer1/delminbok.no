from django import forms
from .models import Book



class BookCreateForm(forms.ModelForm):

    title = forms.CharField(max_length=250, label='Tittel')
    genre = forms.CharField(max_length=20, label='Sjanger')
    draft = forms.BooleanField(required=False, label='Kladd')
    cover_picture = forms.CharField(max_length=1000, required=False, label='Bilde (URL)')
    story = forms.CharField(widget=forms.Textarea, label='Boken')

    class Meta:
        model = Book
        fields = [
            'title',
            'genre',
            'draft',
            'cover_picture',
            'story',
        ]


class BookEditForm(forms.ModelForm):
    title = forms.CharField(max_length=250)
    draft = forms.BooleanField()
    genre = forms.CharField(max_length=20)
    cover_picture = forms.CharField(max_length=1000)
    story = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Book
        fields = [
            'title',
            'draft',
            'genre',
            'cover_picture',
            'story',
        ]