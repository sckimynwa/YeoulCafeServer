from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from .models import Customer


class OrderCoffee(APIView):
    """
    Order Coffee
    """

    def get_customer(self, user):
        try:
            return Customer.objects.get(user=user)
        except Customer.DoesNotExist:
            raise Http404

    def post(self, request):
        customer = self.get_customer(request.user)
        menu = request.data['name']

        if customer.order_coffee(menu=menu):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SignUp(APIView):
    def post(self, request):
        user = User.objects.create_user(
            username=request.data['id'], password=request.data['password'])
        customer = Customer(user=user, name=request.data['name'])

        user.save()
        customer.save()

        token = Token.objects.create(user=user)
        return Response({"Token": token.key})
