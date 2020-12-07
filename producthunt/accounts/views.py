from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def homeacc(request):
    return render(request,'accounts/homeacc.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

# def signup(request):
#     return render(request,'accounts/signup.html')

    # if request.method == 'POST':
    #     #User has the info
    #     if request.POST['password'] == request.POST['conpassword']:
    #         try:
    #             user =  User.objects.get(username=request.POST['username']) 
    #             return render(request,'accounts/signup.html',{'error':'Username is already taken'})
    #         except User.DoesNotExist:
    #             user =   User.Objects.create_user(request.POST['username'],password=request.POST['password'] )
    #             auth.login(request,user)
    #             return redirect('login')
    # else:
    #      return render(request,'accounts/signup.html')
        # user want to get info
 

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    # Todo neet to route to homepage
    return render(request,'accounts/homeacc.html')