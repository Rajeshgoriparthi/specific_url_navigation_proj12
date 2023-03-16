from django.urls import path
from football.views import *
app_name='football'
urlpatterns=[
    path('ronaldo/',ronaldo,name='ronaldo'),
]