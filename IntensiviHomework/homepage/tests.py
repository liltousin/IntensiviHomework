from django.test import Client, TestCase

# Create your tests here.


class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/3213')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/some text-123_')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/3213/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/some text-123_/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('//')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/text/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/text')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/text /')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/text ')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/text asd/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/text asdsd')
        self.assertEqual(response.status_code, 404)

        response = Client().get('3213')
        self.assertEqual(response.status_code, 404)

        response = Client().get('some text-123_')
        self.assertEqual(response.status_code, 404)

        response = Client().get('3213/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('some text-123_/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('text/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('text')
        self.assertEqual(response.status_code, 404)

        response = Client().get('text /')
        self.assertEqual(response.status_code, 404)

        response = Client().get('text ')
        self.assertEqual(response.status_code, 404)

        response = Client().get('text asd/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('text asdsd')
        self.assertEqual(response.status_code, 404)
