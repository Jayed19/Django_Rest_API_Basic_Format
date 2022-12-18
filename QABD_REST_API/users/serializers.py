'''
Serialization is used to convert the data in your Django models into a format(JSON) that can be sent over the internet 
and used by other applications.
'''

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer): #inherit functions from ModelSerializer class
    password=serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data): # This is for making password encrypted
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    class Meta: # For Model indicate
        model=User
        fields=('id','username', 'email', 'password')



        
