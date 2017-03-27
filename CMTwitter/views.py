from django.shortcuts import render, render_to_response

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')