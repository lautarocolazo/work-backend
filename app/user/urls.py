"""
URL mappings for the user API.
"""
from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('get/', views.GetUserView.as_view(), name='get'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
