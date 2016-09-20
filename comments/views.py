from django.shortcuts import render
from .models import Comment


# Create your views here.

def index(request):
    user = request.user
    object_list = Comment.objects.all()

    context = {
        'user': user,
        'object_list':object_list,
    }
    return render(request, "comments/index.html", context)
