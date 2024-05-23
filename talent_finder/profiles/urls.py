from django.urls import path
from . import views

urlpatterns = [
    path('users/<str:name>/', views.get_user_profile),
]
