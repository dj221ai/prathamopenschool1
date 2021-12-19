from os import name
from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('files/', views.excel_list_view, name='files'),
    path('upload/', views.upload_view, name='upload'),
    path('delete/<str:pk>/', views.delete_view, name='delete_file'),
]
