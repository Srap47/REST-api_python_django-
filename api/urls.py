# api/urls.py
from django.urls import path
from .views import create_user, get_users, get_user, update_user, delete_user

urlpatterns = [
    path('users/', get_users, name='get_users'),  # List all users
    path('user/<int:pk>/', get_user, name='get_user'),  # Retrieve a single user
    path('user/create/', create_user, name='create_user'),  # Create a new user
    path('user/<int:pk>/update/', update_user, name='update_user'),  # Update a user
    path('user/<int:pk>/delete/', delete_user, name='delete_user'),  # Delete a user
]
