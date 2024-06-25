from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homepage(request):
  visitor=0
  viewer=visitor+1
  context = {
        'viewer': viewer,
    }
  return render(request, "homepage.html", context)

def about_me(request):
  visitor=0
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "about_me.html", context)

def education(request):
  visitor=0
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "education.html", context)

def skills(request):
  visitor=0
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "skills.html", context)

def contact(request):
  visitor=0
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "contact.html", context)
