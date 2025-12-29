from django.urls import path, include
from . import views
urlspatterns = [
        path('registration/', views.registration)
]