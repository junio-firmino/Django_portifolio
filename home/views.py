from django.shortcuts import render

def metodoViewsHome(request):
    return render(request,'home_tmpl/home.html')
