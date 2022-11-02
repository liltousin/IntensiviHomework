from .models import Category, Item, Tag
from django.core.exceptions import ValidationError
from django.test import Client, TestCase

# Create your tests here.


class StaticURLTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/1/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/983123/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/0/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/0322/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1231/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1qwe/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/1231qwe/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qwee-123/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qwer/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/0322')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1231')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-1qwe')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/1231qwe')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qwee-123')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qwer')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qw  er')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qw  er/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qw  123er/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qw  123er')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qw  123/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/qw  123')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/q-w  -123er/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/q-w  -123er')
        self.assertEqual(response.status_code, 404)


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            is_published=True,
            name='dog',
            slug='123',
            weight=150,
        )
        cls.tag = Tag.objects.create(
            is_published=True,
            name='catt',
            slug='123',
        )

    def test_able_create_one_letter(self):
        self.item = Item(
            name='test',
            category=self.category,
            text='превосходно!')
        self.item.full_clean()
        self.item.save()

    def test_unable_create_one_letter(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(
                name='test',
                category=self.category,
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
            self.item.save()
            self.assertEqual(
                Item.objects.count(),
                item_count)
