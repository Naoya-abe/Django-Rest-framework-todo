from rest_framework.pagination import PageNumberPagination


class TodoListPagination(PageNumberPagination):
    """Return todo items every three cases"""
    page_size = 3
