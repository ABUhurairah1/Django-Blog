from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from .models import Blog,Comment
from django.contrib import messages
from .forms import BlogForm,CommentForm
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm

# Create your views here.

def Home(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'home.html',context)


def Blog_page(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    comments = Comment.objects.filter(blog=blog)
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            blog_comment = form.save(commit=False)
            blog_comment.host = user
            blog_comment.blog = blog
            blog_comment.save()
    else :
        form = CommentForm()

    context = {'blog':blog,'comments' : comments,'form':form}
    return render(request,'blog-page.html',context)

def Comment_delete(request,comment_id):
    comment = Comment.objects.get(id = comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('Home')
    context ={'comment':comment}
    return render(request,'delete-blog.html',context)

@login_required(login_url='Login')
def Add_Blog(request):
    form = BlogForm()
    user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.host = user
            blog.save()
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
    page = "Delete-Blog"
    blog = Blog.objects.get(id = blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('Home')
    context ={'blog':blog,'page':page}
    return render(request,'delete-blog.html',context)

def Comments(request,blog_id):
    blog = Blog.objects.get(id = blog_id)
    comments = Comment.objects.all()
    user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comments.user = user
            comment.blog = blog
            comment.save()

    context = {'comments' : comments,'blog':blog}
    return redirect(request,'blog-page.html',context)

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


