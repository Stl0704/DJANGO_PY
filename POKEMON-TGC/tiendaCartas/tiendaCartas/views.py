from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django import forms

# Create your views here.


def home(request):
    return render(request, 'index.html')


# Sign Up

def signup(request):
    return render(request, 'signup.html')


#Sign In


def signin(request):
    return render(request, 'signin.html')

