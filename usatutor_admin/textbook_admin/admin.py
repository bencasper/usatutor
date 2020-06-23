from django.contrib import admin

# Register your models here.
from .models import TextbookContent
from middleware.admin import TutorCRUDAdmin


@admin.register(TextbookContent)
class TextbookAdmin(TutorCRUDAdmin):
    change_form_template = 'textbook_admin/admin/change_form.html'
    list_display = ('id', 'level_name', 'unit', 'unit_title', 'textbook_title', 'grammar', 'cover_img', 'edit_by')
    search_fields = ['textbook_title']

