from django.urls import path, include
from shoping import views
urlpatterns =[
    path('latestproductlist/', views.latestproductlist.as_view()),
]