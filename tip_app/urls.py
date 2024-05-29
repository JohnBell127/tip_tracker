from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_tip, name='add_tip'),
    
]
