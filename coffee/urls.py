from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', views.CoffeeList.as_view()),
    path('<int:pk>', views.CoffeeDetail.as_view()),
]
