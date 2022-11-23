from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class TagAdmin(admin.ModelAdmin):
    list_display = ('created_on', 'text')
    list_editable = ('text',)
    list_display_links = ('created_on',)
