from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Category, Tag, Article
from .serializers import CategorySerializer, TagSerializer, ArticleSerializer
from .paginations import CategoryPagination, TagPagination, ArticlePagination
from .permissions import IsAuthorOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 
    queryset = Category.objects.all().order_by('-id')


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    pagination_class = TagPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]   
    queryset = Tag.objects.all().order_by('-id')


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    pagination_class = ArticlePagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Article.objects.all().order_by('-id')



