from django.contrib import admin
from django.urls import path,include
from base import views
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.userprofile, name='userprofile'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('logoutPage', views.logoutPage, name='logoutPage'),
    path('room/<str:pk>/', views.room, name = 'room'),
    path('createRoom/', views.createRoom, name = 'createRoom'),
    path('updateRoom/<str:pk>/', views.updateRoom, name = 'updateRoom'),
    path('deleteRoom/<str:pk>/', views.deleteRoom, name = 'deleteRoom')
]
