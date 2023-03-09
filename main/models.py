from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.TextField()
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    footer_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=100, default="------")
    snippet = models.CharField(max_length=255, default="Click the link to read more")
    body = RichTextField(blank=True, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    posted_at = models.DateTimeField(default=datetime.now, blank=True)
    comment = models.TextField()

class Profile(models.Model):
    member = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/")
    bio = models.TextField(blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    discord = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    instagram = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
