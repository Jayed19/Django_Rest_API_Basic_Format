import datetime
from django.db import models


# Create your models here.
class Products(models.Model):
    Product_Name=models.CharField(max_length=150)
    Product_Code=models.CharField(max_length=50,unique=True)
    Product_Description=models.CharField(max_length=500)
    Creation_Date= models.DateTimeField(default=datetime.datetime.today, blank=True)
    Status= models.BooleanField(default=True)
    class Meta:
        db_table = "product"