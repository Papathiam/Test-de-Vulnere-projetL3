from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django import forms

# Create your models here.
class Articles(models.Model):
    titre = models.CharField(max_length=255 , blank=True)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def detailarticle(self):
        return reverse('detailarticle' , args=[self.id])

    def __str__(self):
        return self.titre

class Comment(models.Model):
    articles = models.ForeignKey(Articles, related_name='comments',on_delete=True)
    user = models.OneToOneField(User, on_delete=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def addComment(self):
        return reverse('addComment' , args=[self.id])

    def __str__(self):
        return self.user

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=True)
    email = models.EmailField(max_length=250)
    telephone = models.IntegerField()

    def __str__(self):
        return self.email



class NmapScan(models.Model):
    target = models.CharField(max_length=4048)

    def _str__(self):
        return self.target


# class Blog(models.Model):
#     titre = models.CharField(max_length=255\#     body = models.TextField()
#     image = models.ImageField(upload_to="photos/")

#     def __str__(self):
#         return self.titre


