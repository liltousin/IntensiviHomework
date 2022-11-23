from django.db import models


class Feedback(models.Model):
    text = models.TextField(
        help_text='Введите текст отзыва',
        verbose_name='Отзыв',
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        default_related_name = 'feedbacks'

    def __str__(self) -> str:
        name = self.text.split()[0]
        for word in self.text.split()[1:]:
            if len(name + word) <= 32:
                name += ' ' + word
            else:
                break
        return name
