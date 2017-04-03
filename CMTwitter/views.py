from django.shortcuts import redirect, render, render_to_response

def index(request):
    if request.session.get('logged_in') == None:
        return redirect('/home')
    return render(request, 'index.html')

def home(request):
    if request.session.get('logged_in') != None:
        return redirect('/')
    return render(request, 'home.html')

def profile(request, uid):
    if request.session.get('logged_in') == None:
        return redirect('/home')
    return render(request, 'profile.html')