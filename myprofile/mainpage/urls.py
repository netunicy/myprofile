from .import views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',views.homepage, name='home'),
    path('about_me',views.about_me, name='about_me'),
    path('education',views.education, name='education'),
    path('skills',views.skills, name='skills'),
    path('contact',views.contact, name='contact'),

]