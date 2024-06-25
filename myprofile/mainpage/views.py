from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

view_counts = {
  'homepage': 0,
  'about_me': 0,
  'education': 0,
  'skills': 0,
  'contact': 0,
}

def homepage(request):
  view_counts['homepage'] += 1
  context = {
    'viewer': view_counts['homepage'],
  }
  return render(request, "homepage.html",context)

def about_me(request):
  view_counts['about_me'] += 1
  context = {
    'viewer': view_counts['about_me'],
  }
  return render(request, "about_me.html",context)

def education(request):
  view_counts['education'] += 1
  context = {
    'viewer': view_counts['education'],
  }
  return render(request, "education.html",context)

def skills(request):
  view_counts['skills'] += 1
  context = {
    'viewer': view_counts['skills'],
  }
  return render(request, "skills.html",context)

def contact(request):
  view_counts['contact'] += 1
  context = {
    'viewer': view_counts['contact'],
  }
  return render(request, "contact.html",context)