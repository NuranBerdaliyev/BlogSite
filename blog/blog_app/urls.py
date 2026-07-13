from django.urls import path
from .views import first_view, second_view

urlpatterns = [
    path('', first_view, name='first_view'),
    path('about/', second_view, name='second_view'),
]