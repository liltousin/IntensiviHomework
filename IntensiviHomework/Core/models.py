from django.core.validators import MinValueValidator, RegexValidator
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True, validators=[MinValueValidator(1)])
    is_published = models.BooleanField(
        default=True,
        help_text='Опубликовано ли',
        verbose_name='Публикация',
    )
    name = models.CharField(
        max_length=150,
        help_text='Введите имя',
        verbose_name='Имя',
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        max_length=200,
        validators=[RegexValidator(regex='^[a-z0-9]+(?:[_|-][a-z0-9]+)*$')],
        unique=True,
        help_text='Введите только цифры, буквы латиницы, "-" и "_"',
        verbose_name='Слаг',
    )

    class Meta:
        abstract = True
