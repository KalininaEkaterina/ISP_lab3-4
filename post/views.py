from asgiref.sync import sync_to_async
from django.shortcuts import render, redirect
from .models import Nursery
from .Forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from .Forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import asyncio

from django.contrib.auth import authenticate, login, logout


async def _create_nursery(image, form, request):
    await sync_to_async(Nursery.objects.create)(
        image=image,
        descr=form.data['description'],
        name=form.data['name'],
        user=request.user
    )
    return 0


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Аккаунт уже создан' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'post/register.html', context)

def LoginPase(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Имя пользователя или пароль введен неверно')
                return render(request, 'post/login.html')

    context = {}
    return render(request, 'post/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def index(request):
    nursery = Nursery.objects.order_by('-id')
    return render(request, 'post/index.html', {'title': 'Питомник BouncyKings', 'nursery': nursery})


def about(request):
    return render(request, 'post/about.html')


def our_dog(request):
    return render(request, 'post/our_dog.html')


def puppy(request):
    return render(request, 'post/puppy.html')


def pometkorgi(request):
    return render(request, 'post/pometkorgi.html')


def pometbeagle(request):
    return render(request, 'post/pometbeagle.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверна'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'post/create.html', context)


from django.shortcuts import render

# Create your views here.
