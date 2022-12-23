from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView # Handle HTTP Requests
from rest_framework.response import Response
from django.contrib.auth.models import User 
from .serializers import UserSerializers #import UserSerializer class from serializers.py file
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .paginators import CustomPagination
from rest_framework.permissions import IsAuthenticated

# POST Method and Get All Method
class UserPostRequest(APIView): # Inherit all functions from builtIn APIView Class
    permission_classes = (IsAuthenticated,) # Authentication added Step1
    #Pagination code started
    pagination_class = CustomPagination
    @property
    def paginator(self):
        """The paginator instance associated with the view, or `None`."""
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """Return a single page of results, or `None` if pagination is disabled."""
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """Return a paginated style `Response` object for the given output data."""
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)
    #Pagination code Ended

    
    def get(self, request):
       
        user_all_active = User.objects.all().order_by('id') # All User will show from User table. All is_active=true user will be returen here.
        user_all_active = self.paginate_queryset(user_all_active) # All Userlist with pagination
        
        serializer = UserSerializers(user_all_active, many = True) # check the serializers.py file for checking this UserSerializers class
        #return Response(serializer.data) # Serializer used for converting to JSON format. This Response is without pagination.
        return self.get_paginated_response(serializer.data) # Response with pagination
    
    def post(self, request):
        serializer = UserSerializers(data = request.data) # POST Request data will be store in data variable and serializer object creted with this data
        if serializer.is_valid():
            serializer.save() # Save in the database
            return Response(serializer.data, status = 201) # Created status code 201
        return Response(serializer.errors, status = 400) # Error status code 400, means server error


# Directly One Item Get, Delete and PUT method with Primary Key. Here primary key is 'ID' of User table.
class UserGetPutDelete(APIView):# Inherit all functions from builtIn APIView Class

    def get_object(self, pk): # here pk is the primary key
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None): # This put request also serve the soft delete of user. Recommended to use is_active=false instead of using delete method for inactivating a user.
        snippet = self.get_object(pk)
        #serializer = UserSerializers(snippet, data=request.data) # Meta er modde joto field bola ache shob gular value post request e dite hobe
        serializer = UserSerializers(snippet, data=request.data,partial=True) #partial=True means single field possible to change
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
    pagination_class = CustomPagination #Only one line code inside the class incase of ListAPIView
    def get_queryset(self):
        username = self.kwargs['username'] # ['username'] same like table column name
        return User.objects.filter(username__icontains=username) # For case insensative matching. URL like http://127.0.0.1:8000/users/search/username/jayed/
        
        #return User.objects.filter(username__startswith=username) # For starting text Match
        
        #return User.objects.filter(username=username) # For Exact match


# Partial Search with Non Primary Key Field
class SearchFullName(ListAPIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        Fname = self.kwargs['first_name'] # here ['first_name'] this is the same as table column name. We used first_name as full_name here.
        return User.objects.filter(first_name__icontains=Fname) # For case insensative matching. URL like http://127.0.0.1:8000/users/search/username/jayed/
        
        #return User.objects.filter(username__startswith=username) # For starting text Match
        
        #return User.objects.filter(username=username) # For Exact match


# Partial Search with Non Primary Key Field
class SearchEmail(ListAPIView):
    serializer_class = UserSerializers

    def get_queryset(self):
        E_mail = self.kwargs['email'] # here ['email'] this is the same as table column name. We used first_name as full_name here.
        return User.objects.filter(email__icontains=E_mail) # For case insensative matching. URL like http://127.0.0.1:8000/users/search/username/jayed/
        
        #return User.objects.filter(username__startswith=username) # For starting text Match
        
        #return User.objects.filter(username=username) # For Exact match