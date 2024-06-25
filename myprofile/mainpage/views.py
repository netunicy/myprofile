from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
count = 0 
def homepage(request):
  global count
  count+=1
  context = {
        'viewer':  count,
    }
  return render(request, "homepage.html", context)

def about_me(request):
  global count
  count+=1
  context = {
        'viewer':  count,
    }
  return render(request, "about_me.html", context)

def education(request):
  global count
  count+=1
  context = {
        'viewer':  count,
    }
  return render(request, "education.html", context)

def skills(request):
  global count
  count+=1
  context = {
        'viewer':  count,
    }
  return render(request, "skills.html", context)

def contact(request):
  global count
  count+=1
  context = {
        'viewer':  count,
    }
  return render(request, "contact.html", context)
