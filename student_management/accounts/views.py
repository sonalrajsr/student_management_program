from django.contrib import messages
# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username is unique
        if User.objects.filter(username=username).exists():
            return render(request, 'registeration.html', {'error_message': 'Username already exists'})

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect('login')
    return render(request, 'registeration.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, 'Login successful.')
            return redirect('home')  # Replace 'home' with your home page URL
        else:
            # messages.error(request, 'Invalid login credentials. Please try again.')
            pass

    return render(request, 'login.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('login')