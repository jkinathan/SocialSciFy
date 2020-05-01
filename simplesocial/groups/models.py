from django.db import models
from django.utils.text import slugify

# Create your models here.
#groups models.py file
import misaka

from django.contrib.auth import get_user_model
User = get_user_model() #get current user instance 

from django import template
register = template.Library()



