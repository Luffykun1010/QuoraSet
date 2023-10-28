from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.contrib.auth import authenticate,login,logout
from .models import Posts,Comments
user=User.objects.all()
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('phone')
        password=request.POST.get('password')
        for i in user:
            while i.username == username:
                return redirect('signup')
            else:
                myuser=User.objects.create(username=username,password=password)
                myuser.save()
                return redirect('login')
    return render(request,'signup.html',{'user':user})
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('phone')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:    
            login(request,user)
            return redirect('home')
    return render(request,'login.html')
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user=request.user
            post=request.POST.get('posts')
            new_posts=Posts.objects.create(post=post,user=user)
            new_posts.save()
            return redirect('home')
    else:
        return redirect('login')
    return render(request,'home.html',{'posts':Posts.objects.all(),'comments':Comments.objects.all()})
def comments(request):
    if request.method == 'POST':
        cpost=request.POST.get('commentpost')
        cuser=request.POST.get('commentuser')
        comment=request.POST.get('comments')
        new_comments=Comments.objects.create(user_id=cuser,post_id=cpost,comments=comment)
        new_comments.save()
    return redirect('home')