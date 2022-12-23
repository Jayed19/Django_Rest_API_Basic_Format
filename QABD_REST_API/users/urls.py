from django.urls import path,include,re_path
from .views import UserPostRequest,UserGetPutDelete,SearchUserName,SearchFullName,SearchEmail # Class import from views.py file

urlpatterns = [
    path('', UserPostRequest.as_view()), # UsersAPIView class will be called when browse this link 'http://127.0.0.1:8000/'+'users/' means http://127.0.0.1:8000/users. Please check the qabd_api/urls.py file
    path('getputdel/<int:pk>/', UserGetPutDelete.as_view()),# http://127.0.0.1:8000/users/getputdel/12/ this url for get, put and delete
    re_path('^search/username/(?P<username>.+)/$', SearchUserName.as_view()), #Regex is saying any character or digit will be suppor in the url
    re_path('^search/fullname/(?P<first_name>.+)/$', SearchFullName.as_view()), # Here <first_name> should be the same as table column name. But we used this column for fullname saving.
    re_path('^search/email/(?P<email>.+)/$', SearchEmail.as_view()), # Here <email> should be the same as table column name. Link: http://127.0.0.1:8000/users/search/email/@ymail.com/
]
