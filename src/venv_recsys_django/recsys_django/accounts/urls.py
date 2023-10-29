from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.SignupSuccessView.as_view(), name='signup_success'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]