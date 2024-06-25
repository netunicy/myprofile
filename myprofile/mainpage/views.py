from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def homepage(request):
  count = request.session.get('count', 0)
  count += 1
  request.session['count'] = count
  context = {
    'viewer': count,
  }
  return render(request, "homepage.html",context)

def about_me(request):
  count = request.session.get('count', 0)
  count += 1
  request.session['count'] = count
  context = {
    'viewer': count,
  }
  return render(request, "about_me.html",context)

def education(request):
  count = request.session.get('count', 0)
  count += 1
  request.session['count'] = count
  context = {
    'viewer': count,
  }
  return render(request, "education.html",context)

def skills(request):
  count = request.session.get('count', 0)
  count += 1
  request.session['count'] = count
  context = {
    'viewer': count,
  }
  return render(request, "skills.html",context)

def contact(request):
  count = request.session.get('count', 0)
  count += 1
  request.session['count'] = count
  context = {
    'viewer': count,
  }
  return render(request, "contact.html",context)