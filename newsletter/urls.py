from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('send_newsletter/', views.send_newsletter, name='send_newsletter'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
