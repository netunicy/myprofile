from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homepage(request):
  visitor += 1
  context = {
        'viewer': visitor,
    }
  return render(request, "homepage.html", context)

def about_me(request):
  visitor += 1
  context = {
        'viewer': visitor,
    }
  return render(request, "about_me.html", context)

def education(request):
  visitor += 1
  context = {
        'viewer': visitor,
    }
  return render(request, "education.html", context)

def skills(request):
  visitor += 1
  context = {
        'viewer': visitor,
    }
  return render(request, "skills.html", context)

def contact(request):
  visitor += 1
  context = {
        'viewer': visitor,
    }
  return render(request, "contact.html", context)
