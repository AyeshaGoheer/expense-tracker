from .views import index, expense
from django.urls import path

urlpatterns = [
    path('', index),
    path('expense/', expense, name='expense')
]
