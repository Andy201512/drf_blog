from django.test import TestCase
from .models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='test1')

    def test_Category_name(self):
        category1 = Category.objects.get(id=1)
        self.assertIs(category1.name(), 'test1)
