from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html"), name="login"),
    path('register/', views.RegisterPage, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('profile/', views.ProfilePage, name="profile"),
    path('profile/change_password', views.PasswordChanges, name="change_password"),
    path('accounts/', include('allauth.urls')),
]
