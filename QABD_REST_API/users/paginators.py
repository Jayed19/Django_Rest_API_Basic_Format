from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size' #URL would be http://127.0.0.1:8000/users/search/username/jayed/?page=2 then it will return the result of page 2
    max_page_size = 20 #maximum allowed records count it can return per page.
    page_query_param = 'page' # URL would be http://127.0.0.1:8000/users/search/username/jayed/?page=1&page_size=7 then it will return the result of page 1 and 7 records will be show.