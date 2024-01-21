from .views import *
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
     path("", ChatView.as_view(), name='home'),
     path("login/", LoginView.as_view(), name='login'),
     path("registration/", RegistrationView.as_view(), name='registration'),
     path("logout/", LogoutView.as_view(), name='logout'),
     path("editProfil/<int:pk>", EditProfilView.as_view(), name='editProfil'),
    


]