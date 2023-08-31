from django.urls import path
# from .views import CustomLoginView, CustomLogoutView, CustomRegisterView

from . import views

app_name = 'application'

urlpatterns = [
    path('', views.EntityArrivedHandler),
    path('task_auto_start/', views.task_auto_start),
]