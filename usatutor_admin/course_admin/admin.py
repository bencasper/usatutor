from django.contrib import admin

from .models import CourseContent
from middleware.admin import TutorCRUDAdmin


# @admin.register(CourseContent)
class CourseAdmin(TutorCRUDAdmin):
    list_display = ('id', 'course_name', 'course_desc', 'edit_by')
    fields = ['course_name', 'course_desc']

