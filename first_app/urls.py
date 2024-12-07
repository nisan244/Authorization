from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= 'home'),
    path("signup/", views.user_signup, name= 'user_signup'),
    path("login/", views.user_login, name= 'user_login'),
    path("logout/", views.user_logout, name= 'user_logout'),
    path("profile/", views.user_profile, name= 'profile'),
    path("pass_change/", views.pass_change, name= 'pass_change'),
    path("pass_change_2/", views.pass_change_2, name= 'pass_change_2'),
    
]
