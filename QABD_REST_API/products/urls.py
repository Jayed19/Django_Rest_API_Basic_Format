from django.urls import path,include,re_path
from .views import ProductPostRequest,ProductGetPutDelete,SearchProductName,SearchProductCode 
urlpatterns = [
    path('', ProductPostRequest.as_view()), # UsersAPIView class will be called when browse this link 'http://127.0.0.1:8000/'+'users/' means http://127.0.0.1:8000/users. Please check the qabd_api/urls.py file
    path('getputdel/<int:pk>/', ProductGetPutDelete.as_view()),# http://127.0.0.1:8000/users/getputdel/12/ this url for get, put and delete
    re_path('^search/productname/(?P<Product_Name>.+)/$', SearchProductName.as_view()), #Regex is saying any character or digit will be suppor in the url
    re_path('^search/productcode/(?P<Product_Code>.+)/$', SearchProductCode.as_view()), # Here <first_name> should be the same as table column name. But we used this column for fullname saving.
]
