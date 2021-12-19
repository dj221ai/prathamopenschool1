from . import views
from django.urls import path

app_name = 'account'

urlpatterns = [
    path("register/", views.SignupView.as_view(), name="register"),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
