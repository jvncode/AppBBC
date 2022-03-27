from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product


class TestModelsProduct(TestCase):
    def test_post_has_an_product(self):
        user1 = User.objects.create(username="jvn", password="secret")
        cat1 = Category.objects.create(title='TOY', is_active=False)
        prod1 = Product.objects.create(description="puzzle",
                                       functionality="PER",
                                       category_bk=Category().id,
                                       owner=user1)
        prod2 = Product.objects.create(description="puppet",
                                       functionality="NOR",
                                       category_bk=Category().id,
                                       owner=user1)
        self.assertEqual(Product.objects.values().count(), 2)
