from django.db import models

class PageView(models.Model):
    
    homepage_view_count = models.IntegerField(default=0)
    about_me_view_count = models.IntegerField(default=0)
    education_view_count = models.IntegerField(default=0)
    skills_view_count = models.IntegerField(default=0)
    contact_view_count = models.IntegerField(default=0)
