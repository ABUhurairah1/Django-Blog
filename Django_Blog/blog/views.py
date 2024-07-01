from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from .models import Blog
from django.contrib import messages
from .forms import BlogForm
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm

# Create your views here.

def Home(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'home.html',context)


def Blog_page(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    context = {'blog':blog}
    return render(request,'blog-page.html',context)

def Add_Blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    
    context = {'form' : form}
    return render(request,'add-blog.html',context)

def Update_Blog(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance = blog)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = BlogForm(instance=blog)

    context = {'form':form}
    return render(request,'add-blog.html',context)

def Delete_Blog(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('Home')
    context ={'blog':blog}
    return render(request,'delete-blog.html',context)


def Sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    context = {'form':form}
    return render(request,'sign-up.html',context)

def Login(request):
    User = request.user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(User,username = username,password = password)
        if user != None:
            login(request,user)
            return redirect('Home')

    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('Home')

@login_required(login_url='Login')
def Password_change(request):  
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('Home')
    else:
        form = SetPasswordForm(user=request.user)

    context = {'form':form}
    return render(request,'password_change_form.html',context)


