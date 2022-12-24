'''
Serialization is used to convert the data in your Django models into a format(JSON) that can be sent over the internet 
and used by other applications.
'''

from rest_framework import serializers
from .models import Products

class ProductSerializers(serializers.ModelSerializer): #inherit functions from ModelSerializer class
    Creation_Date=serializers.CharField(read_only=True)
    class Meta: # For Model indicate
        model=Products
        fields=('id','Product_Name', 'Product_Code', 'Product_Description','Status','Creation_Date')






        
