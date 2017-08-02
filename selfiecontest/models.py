# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class SignUp(models.Model):
    full_name= models.CharField(max_length=120)
    email=models.EmailField()
    timestamp=models.DateField(auto_now_add=True,auto_now=False)
    updated=models.DateField(auto_now_add=False,auto_now=True)
    def __unicode__(self):
        return self.email
# Create your models here.

class Picto(models.Model):
    image_id  = models.AutoField(primary_key=True)
    user   = models.ForeignKey(User)
    image  = models.FileField()
    like  = models.IntegerField(default=0) 
    def get_absolute_url(self):
        return reverse('home') 
    def __unicode__(self):
        return unicode(self.user)

class userlike(models.Model):
    like_id=models.AutoField(primary_key=True)
    image_id = models.IntegerField()
    user   = models.ForeignKey(User)
    favourite = models.BooleanField(default="False") 
    def __unicode__(self):
            return unicode(self.user)



class Profile(models.Model):
    """docstring for ClassName"""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic =   models.FileField()
    city = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    def __unicode__(self):
            return unicode(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
