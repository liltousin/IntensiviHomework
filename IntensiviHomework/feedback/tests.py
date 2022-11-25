from django.test import Client, TestCase
from django.urls import reverse
from feedback.models import Feedback

from .forms import FeedbackForm


class FormTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.form = FeedbackForm()
        cls.feedback_count = Feedback.objects.count()
        form_data = {'text': 'Тестовый фидбек'}
        cls.response = Client().post(
            reverse('feedback:feedback'), data=form_data, follow=True
        )

    def test_text_label(self):
        text_label = FormTest.form.fields['text'].label
        self.assertEquals(text_label, 'Отзыв')
        self.assertNotEquals(text_label, 'Отзыв123')

    def test_text_help_text(self):
        text_help_text = FormTest.form.fields['text'].help_text
        self.assertEquals(text_help_text, 'Напишите отзыв')
        self.assertNotEquals(text_help_text, 'Напишите отзыв123')

    def test_form_in_context(self):
        self.assertIn('form', self.response.context)

    def test_redirect(self):
        self.assertRedirects(self.response, reverse('feedback:feedback'))

    def test_add_feedback(self):
        self.assertEqual(self.feedback_count + 1, Feedback.objects.count())
        self.assertTrue(
            Feedback.objects.filter(text='Тестовый фидбек').exists()
        )
