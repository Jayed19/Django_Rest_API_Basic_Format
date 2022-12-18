from django.urls import path,include,re_path
from .views import UsersAPIView,SnippetDetail,PartialUserName

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
    re_path('^field/(?P<username>.+)/$', PartialUserName.as_view()),
]
