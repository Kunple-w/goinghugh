from django.shortcuts import render
from blogs.models import Blogs
# Create your views here.
def index(request):
    # blog = Blogs.objects
    # return render(request,"base.html")
    return render(request,"base.html")
