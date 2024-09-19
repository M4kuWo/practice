from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # Home page at '/'
    path('about/', views.about, name='about'),      # About page at '/about/'
    path('contact/', views.contact, name='contact') # Contact page at '/contact/']
]