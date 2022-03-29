from django.urls import path

from .views import home, user_csv,download

urlpatterns = [

    path('',home),
    path('add/',user_csv),
    path('download/',download)
    
]