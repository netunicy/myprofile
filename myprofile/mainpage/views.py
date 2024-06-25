from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.core.cache import cache

view_counts = {
  'homepage': 0,
  'about_me': 0,
  'education': 0,
  'skills': 0,
  'contact': 0,
}

def homepage(request):
  count = cache.get_or_set('homepage_count', 0)
  cache.set('homepage_count', count + 1)
    
  context = {
    'viewer': count + 1,
  }
  return render(request, "homepage.html",context)

def about_me(request):
  count = cache.get_or_set('about_me_count', 0)
  cache.set('about_me_count', count + 1)
  context = {
    'viewer': count + 1,
  }
  return render(request, "about_me.html",context)

def education(request):
  count = cache.get_or_set('education_count', 0)
  cache.set('education_count', count + 1)
  context = {
    'viewer': count + 1,
  }
  return render(request, "education.html",context)

def skills(request):
  count = cache.get_or_set('skills_count', 0)
  cache.set('skills_count', count + 1)
  context = {
    'viewer': count + 1,
  }
  return render(request, "skills.html",context)

def contact(request):
  count = cache.get_or_set('contact_count', 0)
  cache.set('contact_count', count + 1)
  context = {
    'viewer': count + 1,
  }
  return render(request, "contact.html",context)