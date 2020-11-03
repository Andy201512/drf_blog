from rest_framework.pagenation import PageNumberPagenation


class CategoryPagenation(PageNumberPagenation):
    page_size = 5
    page_size_query_param = 'page_size'


class TagPagenation(PageNumberPagenation):
    page_size = 5
    page_size_query_param = 'page_size'


class ArticlePagenation(PageNumberPagenation):
    page_size = 5
    page_size_query_param = 'page_size'
