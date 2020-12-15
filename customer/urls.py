from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('order_coffee', views.OrderCoffee.as_view()),
    path('signup', views.SignUp.as_view()),
    path('login', views.Login.as_view()),
]
