from django.urls import path
from . import views

app_name='pyapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_attempt/', views.login_attempt, name='login_attempt'),
    path('<int:num>/', views.userlist, name='usuarios'),
    path('register/', views.register, name='new-user'),
    path('register_action/', views.register_action, name='register_action'),
]
