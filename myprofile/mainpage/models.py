from django.db import models
from tinymce.models import HTMLField

class PageView(models.Model):
    
    homepage_view_count = models.IntegerField(default=0)
    about_me_view_count = models.IntegerField(default=0)
    education_view_count = models.IntegerField(default=0)
    skills_view_count = models.IntegerField(default=0)
    contact_view_count = models.IntegerField(default=0)

class About_me(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    text=HTMLField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'About me'
    
    def __str__(self):
        return self.title
class Education(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    text=HTMLField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Education'
    
    def __str__(self):
        return self.title
class Skills(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    text=HTMLField(null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    title=models.CharField(max_length=500,null=True,blank=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    facebook=models.CharField(max_length=500,null=True,blank=True)
    linkedln=models.CharField(max_length=500,null=True,blank=True)
    phone=models.CharField(max_length=500,null=True,blank=True)
    class Meta:
        verbose_name_plural = 'Skills'
    
    def __str__(self):
        return self.title
        
