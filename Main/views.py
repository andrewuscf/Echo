from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect


def home(request, template='base.html'):
    return render(request, template)

def main(request, template='MainPage.html'):
    return render(request, template)

