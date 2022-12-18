from django.urls import path,include
from .views import UsersAPIView,SnippetDetail

urlpatterns = [
    path('', UsersAPIView.as_view()),
    path('snippets/<int:pk>/', SnippetDetail.as_view()),
]
