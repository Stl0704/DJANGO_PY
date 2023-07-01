from django.shortcuts import render

# Create your views here.


def vista_inicio (request):
    return render(request, 'index.html')

# Sign Up

def signup(request):
    return render(request, 'signup.html')


#Sign In


def signin(request):
    return render(request, 'signin.html')