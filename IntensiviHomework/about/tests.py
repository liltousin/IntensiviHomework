from django.test import Client, TestCase

# Create your tests here.


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/about/3213')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/some text-123_')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/3213/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/some text-123_/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about//')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/text/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/text')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/text /')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/text ')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/text asd/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/about/text asdsd')
        self.assertEqual(response.status_code, 404)
