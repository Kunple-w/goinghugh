from django.shortcuts import render,redirect,HttpResponse
from blogs.models import Blogs
from django.core.exceptions import ObjectDoesNotExist
from blogs.forms import NewBlogForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def index(request):
    blog = Blogs.objects.all()
    context = {
        'blogs':blog
    }
    return render(request,"base.html",context=context)
def blog(request,page):
    try:
        blog_detail = Blogs.objects.get(id = page)
    except ObjectDoesNotExist:
        return render(request,'404.html')

    context = {
        'blog_detail':blog_detail
    }
    return render(request,'blog.html',context=context)
def new_blog_form(request):
    form = NewBlogForm
    context = {
        'form':form
    }
    return render(request,'new_blog.html',context = context)
def new_blog_post(request):
    if request.method == "POST":
        form = NewBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog_content = form.cleaned_data['blog_content']
            c = Blogs(title=title,blog_content=blog_content)
            c.save()
            return redirect(to='index')

def index_login(request):
    if request.method == "GET":
        form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('index')
    context = {
        'form':form
    }
    return render(request,'login.html',context)
def index_register(request):
    return HttpResponse('regisger')