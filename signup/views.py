from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout

# Create your views here.
def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('/login')
    return render(request, 'login.html')

def signupUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = name.split()
        name.append('')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('/signup')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('/signup')
        elif not username.isalnum():
            messages.error(request, 'Invalid username!')
            return redirect('/signup')
        else:
            user = User.objects.create(username=username, email=email)
            user.first_name = name[0].capitalize()
            user.last_name = name[1].capitalize()
            user.set_password(password)
            user.save()
            messages.success(request, 'Account Registered Successfully.')
            return redirect('/signup')
    return render(request, 'signup.html')

def logoutUser(request):
    logout(request)
    return loginUser(request)