from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from .models import TextbookContent
from middleware.admin import TutorCRUDAdmin


@admin.register(TextbookContent)
class TextbookAdmin(TutorCRUDAdmin):
    change_form_template = 'textbook_admin/admin/change_form.html'
    list_display = ('id', 'level_name', 'unit', 'unit_title', 'textbook_title', 'grammar', 'image_tag', 'edit_by')
    fields = ('level_name', 'unit', 'unit_title', 'textbook_title', 'grammar', 'cover_img', 'tag',)
    search_fields = ['textbook_title']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="80"/>'.format(obj.cover_img))

    image_tag.short_description = 'Image'

