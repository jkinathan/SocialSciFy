from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
# posts models.py
from groups.models import Group
# import misaka .... this is for markdown text in the text area
from django.contrib.auth import get_user_model
User = get_user_model()   #get current logged in user

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        #self.message_html = misaka.html(self.message)
        #eliminated misaka coz its not working
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username, 'pk':self.pk})
    
    class Meta:
        ordering = ['-created_at'] #minus - is for DESC order
        unique_together = ['user','message']
    
        
    
    

