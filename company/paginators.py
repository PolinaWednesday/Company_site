from rest_framework.pagination import PageNumberPagination


class CompanyPagination(PageNumberPagination):
    """Класс пагинации привычек"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
