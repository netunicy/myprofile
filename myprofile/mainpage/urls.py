from .import views
from django.urls import path

urlpatterns = [
    path('home',views.homepage, name='home'),
    path('about_me',views.about_me, name='about_me'),
    path('education',views.education, name='education'),

]