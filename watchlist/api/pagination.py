from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchlistPagination(CursorPagination):
    page_size = 10
    page_query_param = 'p'
    page_query_description = 'page number'


class WatchlistLOPagination(LimitOffsetPagination):
    default_limit = 5
