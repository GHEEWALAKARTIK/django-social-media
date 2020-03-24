from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('/')
        else:
            return render(request, 'testapp/register.html', {'form': form})
    return render(request, 'testapp/register.html', {'form': form})

# def login(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             request.session['username'] = username
#             auth_login(request, user)
#             return redirect('/')
#         else:
#             messages.error(request, 'Please fill correct username and password!')
#     return render(request, 'testapp/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('/')

def index(request):
    return render(request, 'testapp/home.html')

@login_required
def home(request):
    data = 123
    return render(request, 'testapp/home.html', {'data': data})
