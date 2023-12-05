from rest_framework.pagination import PageNumberPagination


class LMSPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 20
    page_size_query_param = 'page_size'