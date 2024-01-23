from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloWorldSerializer, GreetUserSerializer

# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        data = {"message": "Hello, World!"}
        serializer = HelloWorldSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GreetUser(APIView):
    def get(self, request, username):
        message = f"Hello, {username}!"
        data = {"message": message}
        serializer = GreetUserSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MetaController(APIView):
    def get(self, request):
        hello_data = {"message": "Hello, World!"}
        hello_serializer = HelloWorldSerializer(hello_data)
        username = "John"
        greet_message = f"Hello, {username}!"
        greet_data = {"message": greet_message}
        greet_serializer = GreetUserSerializer(greet_data)
        combined_data = {
            "hello_data": hello_serializer.data,
            "greet_data": greet_serializer.data,
        }
        return Response(combined_data, status=status.HTTP_200_OK)