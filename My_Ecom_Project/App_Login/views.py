from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render,HttpResponsePermanentRedirect
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

from App_Login.models import Profile
from App_Login.forms import Profileform,SignUpForm


# Create your views here.

def sign_up(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('App_Login:login'))
    context={
        'form':form,
    }
    return render(request,'App_Login/sign_up.html',context=context)    

def login_user(request):
    form=AuthenticationForm()
    if request.method =='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse("Logged in ")
    context={
        'form':form,
    }
    return render(request,'App_Login/login.html',context=context)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponse('Logged out')









