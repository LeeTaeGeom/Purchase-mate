from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path("recent_postlist/",recent_postlist , name="recent_postlist"),
    path("makepost/",makepost , name="makepost"),
    
]