from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView # Handle HTTP Requests
from rest_framework.response import Response
from django.contrib.auth.models import User 
from .serializers import UserSerializers #import UserSerializer class from serializers.py file
from django.http import Http404
from rest_framework import status

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



class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
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