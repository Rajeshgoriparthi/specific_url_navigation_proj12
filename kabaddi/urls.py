from django.urls import path
from kabaddi.views import *
app_name='kabaddi'
urlpatterns=[
    path('rahul/',rahul,name='rahul'),
]