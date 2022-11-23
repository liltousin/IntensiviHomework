from django.test import Client, TestCase
from django.urls import reverse
from feedback.models import Feedback

from . import forms


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.form = forms.Form()

    def test_text_label(self):
        text_label = FormTest.form.fields['text'].label
        self.assertEquals(text_label, 'Отзыв')
        self.assertNotEquals(text_label, 'Отзыв123')

    def test_text_help_text(self):
        text_help_text = FormTest.form.fields['text'].help_text
        self.assertEquals(text_help_text, 'Напишите отзыв')
        self.assertNotEquals(text_help_text, 'Напишите отзыв123')

    def test_form_in_context(self):
        form_data = {'text': 'Тестовый фидбек'}
        response = Client().post(
            reverse('feedback:feedback'), data=form_data, follow=True
        )
        self.assertIn('form', response.context)

    def test_redirect(self):
        form_data = {'text': 'Тестовый фидбек'}
        response = Client().post(
            reverse('feedback:feedback'), data=form_data, follow=True
        )
        self.assertRedirects(response, reverse('feedback:feedback'))

    def test_add_feedback(self):
        feedback_count = Feedback.objects.count()
        form_data = {'text': 'Тестовый фидбек'}
        Client().post(
            reverse('feedback:feedback'), data=form_data, follow=True
        )
        self.assertEqual(feedback_count + 1, Feedback.objects.count())
        self.assertTrue(
            Feedback.objects.filter(text='Тестовый фидбек').exists()
        )
