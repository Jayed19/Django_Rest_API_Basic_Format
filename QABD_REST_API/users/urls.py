from django.urls import path,include,re_path
from .views import UserPostRequest,UserGetPutDelete,SearchUserName # Class import from views.py file

urlpatterns = [
    path('', UserPostRequest.as_view()), # UsersAPIView class will be called when browse this link 'http://127.0.0.1:8000/'+'users/' means http://127.0.0.1:8000/users. Please check the qabd_api/urls.py file
    path('getputdel/<int:pk>/', UserGetPutDelete.as_view()),
    re_path('^search/username/(?P<username>.+)/$', SearchUserName.as_view()), #Regex is saying any character or digit will be suppor in the url
]
