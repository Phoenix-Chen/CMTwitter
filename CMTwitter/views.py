from django.shortcuts import render, render_to_response

def index(request):
    print("1")
    if request.session.get('logged_in', False):
        print("2")
        return redirect('/home')
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')