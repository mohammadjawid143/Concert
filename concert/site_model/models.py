from django.db import models
from django.contrib import admin

# Create your models here.

class site_setting(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    about_us = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    copy_right= models.TextField()
    site_logo = models.ImageField(upload_to="Side_Logo/")
    Main_setting = models.BooleanField()
    
    
    class Meta:
        verbose_name = 'Site_Settings'
    def __str__(self):
        return self.site_name
    
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} {self.surname} ({self.email})"
