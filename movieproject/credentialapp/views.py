from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid')

    return render(request, 'login.html')


def register(request):
    # add to database
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                # auth table creation
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                print('user created')
                return redirect('/')


        else:
            messages.info(request, "PASSWORD NOT MATCHING")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

