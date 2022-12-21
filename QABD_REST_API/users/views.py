from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView # Handle HTTP Requests
from rest_framework.response import Response
from django.contrib.auth.models import User 
from .serializers import UserSerializers #import UserSerializer class from serializers.py file
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveAPIView


# POST Method and Get All Method
class UserPostRequest(APIView): # Inherit all functions from builtIn APIView Class
    def get(self, request):
        user_all = User.objects.all() # All User will show from User table. Pagination mentioned in the qabd_api/settings.py file
        serializer = UserSerializers(user_all, many = True) # check the serializers.py file for checking this UserSerializers class
        return Response(serializer.data) # Serializer used for converting to JSON format
    
    def post(self, request):
        serializer = UserSerializers(data = request.data) # POST Request data will be store in data variable and serializer object creted with this data
        if serializer.is_valid():
            serializer.save() # Save in the database
            return Response(serializer.data, status = 201) # Created status code 201
        return Response(serializer.errors, status = 400) # Error status code 400, means server error


# Directly One Item Get, Delete and PUT method with Primary Key. Here primary key is 'ID' of User table.
class UserGetPutDelete(APIView):# Inherit all functions from builtIn APIView Class

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Partial Search with Non Primary Key Field
class SearchUserName(ListAPIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        username = self.kwargs['username']
        return User.objects.filter(username__icontains=username) # For case insensative matching. URL like http://127.0.0.1:8000/users/search/username/jayed/
        
        #return User.objects.filter(username__startswith=username) # For starting text Match
        
        #return User.objects.filter(username=username) # For Exact match


