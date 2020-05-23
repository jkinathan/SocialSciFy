from django.db import models
from django.utils.text import slugify

# Create your models here.
#groups models.py file
#import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
User = get_user_model() #get current user thats logged in

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default="")
    description_html = models.TextField(editable=False, default="", blank=True)
    members = models.ManyToManyField(User,through="GroupMember")
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})
    
    #once someone has saved a group, where to send them is why we use get_absolute_url
    
    class Meta:
        ordering = ['name']
    
        

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships", on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_groups")
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group','user')

