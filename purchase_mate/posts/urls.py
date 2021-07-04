from django.urls import path
from .views import *
from django.utils import timezone

app_name = "posts"

urlpatterns = [
    path("recent_postlist/",recent_postlist,name="recent_postlist"),
    path("makepost/",makepost,name="makepost"),
    path("<str:id>",detail,name="detail"),
    path("create/",create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>',update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('category/food/',food,name="food"),
    path('category/daily_necessity/',daily_necessity,name="daily_necessity"),
    path('category/ott/',ott,name="ott"),
    path('category/etc/',etc,name="etc"),
]