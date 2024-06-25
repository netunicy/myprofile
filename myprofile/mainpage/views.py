from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homepage(request):
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "homepage.html", context)

def about_me(request):
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "about_me.html", context)

def education(request):
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "education.html", context)

def skills(request):
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "skills.html", context)

def contact(request):
  viewer=viewer+1
  context = {
        'viewer': viewer,
    }
  return render(request, "contact.html", context)
