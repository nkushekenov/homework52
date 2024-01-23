from rest_framework import serializers

class HelloWorldSerializer(serializers.Serializer):
    message = serializers.CharField()

class GreetUserSerializer(serializers.Serializer):
    message = serializers.CharField()