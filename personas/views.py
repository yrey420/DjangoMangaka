from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_view
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms.utils import ErrorList


from personas.forms import LoginForm, SignUpForm


# Create your views here.
from personas.models import LocalUser


@login_required
def bienvenida(request):
    return render(request, 'personas/bienvenida.html')


def index(request):
    return render(request, 'personas/index.html')


@login_required
def reset(request):
    return  render(request, 'personas/reset_password.html')


@login_required
def logout(request):
    return  render(request, 'personas/logout.html')





def login(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login_view(request, user)
                return redirect("/personas/bienvenida")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'error validanting the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User Created!'
            success = True
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, 'accounts/register.html', {"form": form, "msg": msg, "success": success})


def forgotPassword(request):
    return render(request, 'personas/forgot-password.html')


def e404(request):
    return render(request, 'personas/404.html')


def blank(request):
    return render(request, 'personas/blank.html')



