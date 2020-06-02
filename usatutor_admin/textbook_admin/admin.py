from django.contrib import admin

# Register your models here.
from .models import TextbookContent


@admin.register(TextbookContent)
class TextbookAdmin(admin.ModelAdmin):

    pass
