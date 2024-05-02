from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name="home"),
    path('login/',views.loginPage, name="login"),
    path('register/',views.registerPage, name="register"),
    path('logout/',views.logoutUser, name="logout"),
    path('room/<str:pk>', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name="delete-room"),
]