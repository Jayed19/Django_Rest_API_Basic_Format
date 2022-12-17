from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView # Handle HTTP Requests
from rest_framework.response import Response
from django.contrib.auth.models import User 
from .serializers import UserSerializers #import UserSerializer class from serializers.py file

class UsersAPIView(APIView): # Inherit all functions from APIView Class
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many = True)
        return Response(serializer.data) # Serializer used for converting to JSON format
    
    def post(self, request):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save() # Save in the database
            return Response(serializer.data, status = 201) # Created status code 201
        return Response(serializer.errors, status = 400) # Error status code 400, means server error



