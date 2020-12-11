from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Customer


class OrderCoffee(APIView):
    """
    Order Coffee
    """

    def get_customer(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        customer = self.get_customer(pk)
        menu = request.data['name']
        if customer.order_coffee(menu=menu):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
