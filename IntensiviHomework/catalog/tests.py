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


class 