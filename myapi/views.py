from django.shortcuts import render
from myapi.forms import *
from django.core.mail import send_mail
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.

def register(request):
    registered=False
    userform=UserForm()
    profileform=ProfileForm()
    if request.method=='POST' and request.FILES:#checking post and filess
        userform=UserForm(request.POST)# collecting data of userform
        profileform=ProfileForm(request.POST,request.FILES)# collecting data of profile form
        if userform.is_valid() and profileform.is_valid():# validating both collected data
            user=userform.save(commit=False)#creating obj of userform class which do not updated in db
            user.set_password(userform.cleaned_data['password'])#encrypting of users password
            user.save()#saving all the data OF USER into DB
            profile=profileform.save(commit=False)#CREATING OBJ OF PROFILE FORM CLASS
            profile.user=user#EXTRACTING DATA FORM USER AND STORE IT IN PRIFILES USER
            profile.save()#saving all the data OF PROFILE into DB

            send_mail('registration',
                       'REG IS SUCCESSFULL THANKS FIR REG',
                       'avetasukumar308@gmail.com',
                       [user.email]  ,
                       fail_silently=False)
            registered=True           

    d={'registered':registered,'userform':userform,'profileform':profileform}
    return render(request,'register.html',context=d)


def home(request):
    return render(request,'home.html')



def login(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user and user.is_active:
                login(request,user)
                request.session['usename']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('not a active user')
    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

