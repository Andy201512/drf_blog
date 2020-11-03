from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CategorySerializer, TagSerializer, ArticleSerializer
from .paginations import CategoryPagination, TagPagination, ArticlePagination
from .permissions import IsAuthorOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    pagination_class = TagPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]



