from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . models import Song
from .forms import CreateUserForm



def index(request):
    return render(request, 'index.html')

def games(request):
    if request.user.is_authenticated:
        return render(request, 'games.html')
    else:
        return redirect('/signup')

def signup(request):
	if request.user.is_authenticated:
		context = {"signupMessage":"You are already logged in, please logout to continue."}
		return redirect('/loggedin')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')[0]
				messages.success(request, 'Account was created for ' + user)

				return redirect('/login')
		context = {'form':form}
		return render(request, 'signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('/')

def loggedin(request):
	return render(request, 'loggedin.html')

def blog(request):
    if request.user.is_authenticated:
        return render(request, 'blog.html')
    else:
        return redirect('/signup')

def music(request):
	if request.user.is_authenticated:
		paginator= Paginator(Song.objects.all(),1)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context={"page_obj":page_obj}
		return render(request, "music.html", context)
	else:
		return redirect('/signup')
