from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

homepage = {
    'homepage': 0
}

about_me = {
    'about_me': 0
}

education = {
    'education': 0
}

skills = {
    'skills': 0
}

contact = {
    'contact': 0
}

def homepage(request):
  homepage['homepage'] += 1
  context = {
    'viewer': homepage['homepage'],
  }
  return render(request, "homepage.html",context)

def about_me(request):
  about_me['about_me'] += 1
  context = {
    'viewer': about_me['about_me'],
  }
  return render(request, "about_me.html",context)

def education(request):
  education['education'] += 1
  context = {
    'viewer': education['education'],
  }
  return render(request, "education.html",context)

def skills(request):
  skills['skills'] += 1
  context = {
    'viewer': skills['skills'],
  }
  return render(request, "skills.html",context)

def contact(request):
  contact['contact'] += 1
  context = {
    'viewer': contact['contact'],
  }
  return render(request, "contact.html",context)