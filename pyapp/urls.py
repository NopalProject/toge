from django.urls import path
from . import views

app_name='pyapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('<int:num>/', views.userlist, name='usuarios'),
]
