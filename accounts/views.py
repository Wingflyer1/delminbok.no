from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm

app_name = 'accounts'

def login_view(request):
    title = 'Logg inn'
    form = UserLoginForm(request.POST or None)
    register = True
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        # print(request.user.is_authenticated())
        return redirect("stories:my_page")
    # redirect
    context = {
        'form':form,
        'title':title,
        'message':register,
    }

    return render(request, "form.html", context)


def register_view(request):
    title = 'Registrering'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("stories:my_page")

    context = {
        'form':form,
        'title':title,
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("accounts:login")