from .models import Coffee
from .serializers import CoffeeSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class CoffeeList(APIView):
    """
    List all coffee 
    """

    def get(self, request):
        coffee = Coffee.objects.all()
        serializer = CoffeeSerializer(coffee, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoffeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoffeeDetail(APIView):
    """
    Get, Update, Delete Coffee
    """

    def get_object(self, pk):
        try:
            return Coffee.objects.get(pk=pk)
        except Coffee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        coffee = self.get_object(pk)
        serializer = CoffeeSerializer(coffee)
        return Response(serializer.data)

    def put(self, request, pk):
        coffee = self.get_object(pk)
        serializer = CoffeeSerializer(coffee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        coffee = self.get_object(pk)
        coffee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
