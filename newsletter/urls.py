from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/', views.subscribe, name='subscribe'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
