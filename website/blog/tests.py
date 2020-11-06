from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.conf import settings
import os

from rest_framework.test import APITestCase
from .models import Category, Tag, Article


# Models tests
class CategoryModelTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='Category_test1')

    def test_Category_name(self):
        category1 = Category.objects.get(id=1)
        self.assertEqual(category1.name, 'Category_test1')


class TagModelTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name='Tag_test1')
    
    def test_Tag_name(self):
        tag1 = Tag.objects.get(id=1)
        self.assertEqual(tag1.name, 'Tag_test1')


class ArticleModelTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='admin', password='123')
        test_image = SimpleUploadedFile(name='test_foo.jpg', content=b'bar', content_type='image/jpeg')
        Article.objects.create(title='Article_test1', author=test_user, img=test_image)
    
    def tearDown(self):
        article1 = Article.objects.get(id=1)
        print(settings.MEDIA_ROOT/str(article1.img))
        os.remove(settings.MEDIA_ROOT/str(article1.img))
        print('test image has been removed')

    def test_Article_fileds(self):
        article1 = Article.objects.get(id=1)


# API tests
class CategoryAPITestCase(APITestCase):
    def setUp(self):
        Category.objects.create(name='Category_test1')
    
    def test_Category_API(self):
        url = 'http://blog/api/v1/categorys/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TagAPITestCase(APITestCase):
    def setUp(self):
        Tag.objects.create(name='Tag_test1')
    
    def test_Tag_API(self):
        url = 'http://blog/api/v1/tags/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ArticleAPITestCase(APITestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='admin', password='123')
        test_image = SimpleUploadedFile(name='test_foo.jpg', content=b'bar', content_type='image/jpeg')
        Article.objects.create(title='Article_test1', author=test_user, img=test_image)
    
    def tearDown(self):
        article1 = Article.objects.get(id=1)
        print(settings.MEDIA_ROOT/str(article1.img))
        os.remove(settings.MEDIA_ROOT/str(article1.img))
        print('test image has been removed')
        
    def test_Article_API(self):
        url = 'http://blog/api/v1/articles/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

