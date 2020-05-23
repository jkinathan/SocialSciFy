from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic  #these are the class based views
from .models import Group,GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name', 'description') #these are the fields to edit from the model
    model = Group

class SingleGroup(generic.DetailView):  #details of a single group
    model = Group

class ListGroup(generic.ListView):    #this is for a list of all groups
    model = Group
          