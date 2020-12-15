from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('<int:pk>', views.OrderCoffee.as_view()),
]
