from django.test import TestCase
from .models import *

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category_name='Food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))


