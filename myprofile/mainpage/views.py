
from django.shortcuts import render
#from mainpage.models import PageView
#from .models import About_me,Education,Skills,Contact


def homepage(request):
  #viewer, created = PageView.objects.get_or_create(pk=1)
  #viewer.homepage_view_count += 1
  #viewer.save()
  #context = {
    #'viewer': viewer.homepage_view_count,
  #}
  return render(request, "homepage.html")

def about_me(request):
  #viewer, created = PageView.objects.get_or_create(pk=1)
  #data=About_me.objects.all().values()
  #viewer.about_me_view_count += 1
  #viewer.save()
  #context = {
    #'viewer': viewer.about_me_view_count,
    #'data':data,
  #}
  return render(request, "about_me.html")

def education(request):
  #viewer, created = PageView.objects.get_or_create(pk=1)
  #data=Education.objects.all().values()
  #title = Education.objects.values_list('title', flat=True).first()
  #viewer.education_view_count += 1
  #viewer.save()
  #context = {
    #'viewer': viewer.education_view_count,
    #'data':data,
    #'title':title,
  #}
  return render(request, "education.html")

def skills(request):
  #viewer, created = PageView.objects.get_or_create(pk=1)
  #viewer.skills_view_count += 1
  #viewer.save()
  #data=Skills.objects.all().values()
  #title = Skills.objects.values_list('title', flat=True).distinct()
  #context = {
    #'viewer': viewer.skills_view_count,
    #'data':data,
    #'title':title,
  #}
  return render(request, "skills.html")

def contact(request):
  #viewer, created = PageView.objects.get_or_create(pk=1)
  #viewer.contact_view_count += 1
  #viewer.save()
  #data=Contact.objects.all().values()
  #title = Contact.objects.values_list('title', flat=True).first()
  #context = {
    #'viewer': viewer.contact_view_count,
    #'data':data,
    #'title':title,
  #}
  return render(request, "contact.html")