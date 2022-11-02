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

    def test_unable_create_one_letter(self):
        item_count = Item.objects.count()
        with self.assertRaises(ValidationError):
            self.item = Item(name='test', category=self.category,
                             text='пквыкен')
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)
            self.item.save()
        self.assertEqual(Item.objects.count(), item_count)

        with self.assertRaises(ValidationError):
            self.item_2 = Item(name='test', category=self.category,
                               text='пквыкен')
            self.item_2.full_clean()
            self.item_2.save()
            self.item_2.tags.add(self.tag)
            self.item_2.save()
        self.assertEqual(Item.objects.count(), item_count)

        with self.assertRaises(ValidationError):
            self.item_3 = Item(name='test', category=self.category,
                               text='пквыкен')
            self.item_3.full_clean()
            self.item_3.save()
            self.item_3.tags.add(self.tag)
            self.item_3.save()
        self.assertEqual(Item.objects.count(), item_count)

        with self.assertRaises(ValidationError):
            self.item_4 = Item(name='test', category=self.category,
                               text='сидит прЕ!восходно!')
            self.item_4.full_clean()
            self.item_4.save()
            self.item_4.tags.add(self.tag)
            self.item_4.save()
        self.assertEqual(Item.objects.count(), item_count)


    def test_able_create_one_letter(self):
        item_count = Item.objects.count()
        self.item = Item(name='test', category=self.category,
                         text='превосходно сидит на всех')
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)
        self.item.save()
        self.assertEqual(Item.objects.count(), item_count + 1)

        self.item_2 = Item(name='test', category=self.category,
                           text='превосходно! сидит на всех')
        self.item_2.full_clean()
        self.item_2.save()
        self.item_2.tags.add(self.tag)
        self.item_2.save()
        self.assertEqual(Item.objects.count(), item_count + 2)
