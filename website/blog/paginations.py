from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class TagPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class ArticlePagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
