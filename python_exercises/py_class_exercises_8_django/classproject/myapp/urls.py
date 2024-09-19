from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.redirect_to_index, name='index_redirect'),  # Serve index.html at the root URL
    path('register/', views.register, name='register'),  # Registration URL
    path('superheroes/', views.superhero_list, name='superhero_list'),
    path('superheroes/<int:id>/', views.superhero_detail, name='superhero_detail'),
    path('creatures/', views.creatures_list, name='creatures_list'),
    path('creatures/<int:id>/', views.creatures_detail, name='creatures_detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
