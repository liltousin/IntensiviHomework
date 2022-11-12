from catalog.validators import validate_must_be_param
from Core.models import BaseModel, SlugMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


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

    upload = models.ImageField(
        upload_to='uploads/%Y/%m', verbose_name='превью'
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(f'<img src="{self.get_img.url}"')
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        default_related_name = 'items'


class Tag(BaseModel, SlugMixin):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        default_related_name = 'tags'


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
        default_related_name = 'categorys'


class Gallery(models.Model):
    image = models.ImageField(
        verbose_name='изображение', help_text='Загрузить картинку', null=True
    )
    item = models.ForeignKey(
        Item,
        verbose_name='товар',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'галлерея'
        default_related_name = 'gallary'
