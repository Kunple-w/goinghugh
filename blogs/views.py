from django.shortcuts import render,redirect,HttpResponse
from blogs.models import Blogs,Article
from django.core.exceptions import ObjectDoesNotExist
from blogs.forms import NewBlogForm,ArticleForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    blog = Blogs.objects.all()
    context = {
        'blogs':blog
    }
    return render(request,"base.html",context=context)
def blog(request,page):
    articleForm = ArticleForm
    try:
        blog_detail = Blogs.objects.get(id = page)
        articles = blog_detail.article_to_blog.all()
    except ObjectDoesNotExist:
        return render(request,'404.html')
    context = {
        'blog_detail':blog_detail,
        'article_form':articleForm,
        'articles':articles,
    }
    print(articles)
    return render(request,'blog.html',context=context)
def article_to_blog(request,id):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            articler_pst = form.cleaned_data['articler']
            article_pst = form.cleaned_data['article_content']
            blog = Blogs.objects.get(id=id)
            print(article_pst,articler_pst)
            a = Article(articler=articler_pst,article_content=article_pst,article_to_blog=blog)
            a.save()
        return redirect(to='blog',page=id)
    return render(request, 'blog.html')
@login_required
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
            blog_digest = form.cleaned_data['blog_degist']
            blog_content = form.cleaned_data['blog_content']
            c = Blogs(title=title,blog_digest=blog_digest,blog_content=blog_content)
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
    logout(request)
    return render(request,'register.html')