from catalog.models import Category, Gallery, Item, Tag
from django.contrib import admin
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class PhotoGaleryinline(admin.TabularInline):
    model = Gallery
    fk_name = 'item'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)

    inlines = [PhotoGaleryinline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)


@admin.register(Gallery)
class GallaryAdmin(admin.ModelAdmin):
    list_display = ('item', 'image', 'image_thb')
    list_editable = ('image',)

    def get_img(self, obj):
        return get_thumbnail(obj.image, '300x300', crop='center', quality=51)

    def image_thb(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{self.get_img(obj).url}">')
        return 'Нет изображения'

    image_thb.short_description = 'фото'
    image_thb.allow_tags = True
