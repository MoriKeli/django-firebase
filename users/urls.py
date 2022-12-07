from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserLogin.as_view(), name='login'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('create-account/', views.signup_view, name='signup'),

]
