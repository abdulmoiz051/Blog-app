from django.shortcuts import render,redirect,get_object_or_404
from django.http import request
from .forms import login_system,blog_form,update_delete_user
from .models import blog
from django.contrib.auth import login
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import get_user_model

Own_User = get_user_model()
# Create your views here.

# ORM is a very honest and peaceful and this is my favourate and when i saw his magic i have ever and never shock but this time this is my favourate relationship between python classes and database means sqlite tables

def app(request):
    return render(request,'app.html')

def register(request):
    if request.method == 'POST':
        create = login_system(request.POST,request.FILES)
        if create.is_valid():
            final = create.save(commit=False)
            final.set_password(create.cleaned_data['password1'])
            final.save()
            login(request,final)
            return redirect('app')
    else:
        create = login_system()
    return render(request,'registration/register.html',{'create' : create})

def query(request):
    all_blog_list = blog.objects.all().order_by('-created')
    return render(request,'app.html',{'all_blog_list': all_blog_list})

@login_required
def create_blog(request):
    if request.method == "POST":
        create = blog_form(request.POST,request.FILES)
        if create.is_valid():
            form = create.save(commit=False)
            form.User = request.user
            form.save()
            return redirect('app')
    else:
        create = blog_form()
    return render(request,'create_blog.html',{'create': create})

@login_required
def blog_update(request,blog_update):
    update = get_object_or_404(blog,pk=blog_update,User = request.user)
    if request.method == "POST":
        create = blog_form(request.POST,request.FILES,instance=update)
        if create.is_valid():
            form = create.save(commit=False)
            form.User = request.user
            form.save()
            return redirect('app')
    else:
        create = blog_form(instance=update)
    return render(request,'create_blog.html',{'create':create})

@login_required
def blog_delete(request,delete_blog):
    delete_blog = get_object_or_404(blog,pk=delete_blog,User = request.user)
    if request.method == 'POST':
        delete_blog.delete()
        return redirect('app')
    return render(request,'delete.html',{'delete_blog':delete_blog})

@login_required
def profile_change(request,id_profile):
    query_id = get_object_or_404(Own_User,pk=id_profile)
    if request.method == 'POST':
        form = update_delete_user(request.POST,request.FILES,instance=query_id)
        if form.is_valid():
            form.save()
            return redirect('app')
    else:
        form = login_system(instance=query_id) 
    return render(request,'registration/profile_change.html',{'form':form})