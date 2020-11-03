from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import CategorySerializer, TagSerializer, ArticleSerializer
from .pagenations import CategoryPagenation, TagPagenation, ArticlePagenation
from .permissions import IsAuthorOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    pagenation_class = CategoryPagenation
    permission_classes = [permissions.IsAuthenticateOrReadOnly]


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    pagenation_class = TagPagenation
    permission_classes = [permissions.IsAuthenticateOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    pagenation_class = ArticlePagenation
    permission_classes = [permissions.IsAuthenticateOrReadOnly, IsAuthorOrReadOnly]



