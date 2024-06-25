from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homepage(request):
  viewer=viewer+1
  return render(request, "homepage.html")

def about_me(request):
  viewer=viewer+1
  return render(request, "about_me.html")

def education(request):
  viewer=viewer+1
  return render(request, "education.html")

def skills(request):
  viewer=viewer+1
  return render(request, "skills.html")

def contact(request):
  viewer=viewer+1
  return render(request, "contact.html")
