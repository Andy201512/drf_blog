from .models import Category, Tag, Article
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class TagSerializer(serializers.ModelSerializer):
    class Mate:
        model = Tag
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source='category.name')
    tag = serializers.ReadOnlyField(source='tag.name')
    author = serializers.ReadOnlyField(source='author.name')

    class Mate:
    model = Article
    fields = ['id', ' author', 'created_time', 'modifyed_time', 'excerpt', 'category', 'tags',
              'views', 'img', 'body']