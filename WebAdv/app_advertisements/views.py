from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

def post_advertisement(request):
    return render(request, 'advertisement-post.html')

def register(request):
    return render(request, 'register.html')