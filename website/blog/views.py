from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Tag, Article
from .serializers import CategorySerializer, TagSerializer, ArticleSerializer
from .paginations import CategoryPagination, TagPagination, ArticlePagination
from .permissions import IsAuthorOrReadOnly

import markdown


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
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        instance.increase_views()
        instance.body = markdown.markdown(instance.body,
                         extensions=[
                             'markdown.extensions.extra',
                             'markdown.extensions.codehilite',
                             'markdown.extensions.toc'
                         ])
        return Response(serializer.data)


