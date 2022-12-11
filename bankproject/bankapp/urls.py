from django.urls import path
from . import views
from .models import place
from .views import form

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
    # path('add/',views.addition, name='addition'),
]
