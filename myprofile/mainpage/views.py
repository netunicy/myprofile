from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homepage(request):
  return render(request, "homepage.html")

def about_me(request):
  return render(request, "about_me.html")

def education(request):
  return render(request, "education.html")

def skills(request):
  return render(request, "skills.html")