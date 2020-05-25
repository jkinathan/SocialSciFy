#Groups url file
from django.conf.urls import url
from django.urls import path
from . import views

app_name = "groups" #this is for referencing in url templating

urlpatterns = [
    path('',views.ListGroup.as_view(),name="all"),
    path('new/',views.CreateGroup.as_view(),name="create"),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name="single"),
]
