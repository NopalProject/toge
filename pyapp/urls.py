from django.urls import path
from . import views

app_name='pyapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_attempt/', views.login_attempt, name='login_attempt'),
    path('ajax_test/', views.ajax_test, name='ajax_test'),
    path('register/', views.register, name='new-user'),
    path('register_action/', views.register_action, name='register_action'),
    path('logout_action/', views.logout_action, name='logout_action'),
    path('my_notes/', views.my_notes, name='my_notes'),
]
