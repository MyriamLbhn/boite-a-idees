from django.urls import path
from django.contrib.auth import views as auth_views

from userapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name = 'logout'),
    # path('register/', views.register, name='register'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    path('ajout/', views.ajouter_idee, name='ajout'),


]