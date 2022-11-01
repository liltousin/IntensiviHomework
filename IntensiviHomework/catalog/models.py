from catalog.validators import validate_must_be_param
from Core.models import BaseModel, SlugMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Item(BaseModel):
    text = models.TextField(
        validators=[validate_must_be_param('превосходно', 'роскошно')],
        help_text='Введите описание товара',
        verbose_name='Описание товара',
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='items',
        help_text='Введите категорию',
        verbose_name='Категория',
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='items',
        help_text='Введите тэг',
        verbose_name='Тэги',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Tag(BaseModel, SlugMixin):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(BaseModel, SlugMixin):
    weight = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(32767)],
        help_text='Введите вес категории',
        verbose_name='Вес категории',
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
