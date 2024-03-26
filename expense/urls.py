from .views import index, expense, report
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('report/', report, name='report'),
    path('api/expense/', expense, name='expense-api')
]
