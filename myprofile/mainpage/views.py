
from django.shortcuts import render
from mainpage.models import PageView
from .models import About_me,Education,Skills,Contact


def homepage(request):
  viewer, created = PageView.objects.get_or_create(pk=1)
  viewer.homepage_view_count += 1
  viewer.save()
  context = {
    'viewer': viewer.homepage_view_count,
  }
  return render(request, "homepage.html",context)

def about_me(request):
  viewer, created = PageView.objects.get_or_create(pk=1)
  data=About_me.objects.all().values()
  viewer.about_me_view_count += 1
  viewer.save()
  context = {
    'viewer': viewer.about_me_view_count,
    'data':data,
  }
  return render(request, "about_me.html",context)

def education(request):
  viewer, created = PageView.objects.get_or_create(pk=1)
  viewer.education_view_count += 1
  viewer.save()
  context = {
    'viewer': viewer.education_view_count,
  }
  return render(request, "education.html",context)

def skills(request):
  viewer, created = PageView.objects.get_or_create(pk=1)
  viewer.skills_view_count += 1
  viewer.save()
  context = {
    'viewer': viewer.skills_view_count,
  }
  return render(request, "skills.html",context)

def contact(request):
  viewer, created = PageView.objects.get_or_create(pk=1)
  viewer.contact_view_count += 1
  viewer.save()
  context = {
    'viewer': viewer.contact_view_count,
  }
  return render(request, "contact.html",context)