from django.urls import path
from .views import main, about

urlpatterns = [
    path('main/', main, name='main'),
    path('about/', about, name='about'),
]