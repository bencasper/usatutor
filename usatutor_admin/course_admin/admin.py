from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import get_user
from django.forms import ModelForm

from .models import CourseContent


@admin.register(CourseContent)
class CourseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.edit_by = get_user(request).username
        obj.save()

    def _get_base_actions(self):
        return []

    list_display = ('id', 'course_name', 'course_desc', 'edit_by')
    fields = ['course_name', 'course_desc']

