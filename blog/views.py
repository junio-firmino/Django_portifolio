from django.shortcuts import render
from django.http import HttpResponse

def metodo_views_blog(request):
    return render(request,'blog_tmpl/blog.html')
