# Register your models here.
from course_admin.models import CourseContent
from django import forms
from django.contrib import admin

from .models import UserTutorSchedule


@admin.register(UserTutorSchedule)
class UserScheduleAdmin(admin.ModelAdmin):
    change_list_template = "my_schedule/admin/my_schedule.html"

    @property
    def media(self):
        js = [
            'moment.min.js',
            'jquery.min.js',
            'jquery-ui.min.js',
            'fullcalendar.min.js',
            'scheduler.min.js',
            'jquery-confirm.min.js'
        ]
        css = [
            'fullcalendar.min.css',
            'scheduler.min.css',
            'jquery-ui.css',
            'jquery-confirm.min.css',
        ]
        return forms.Media(css={'all': ['schedule/css/%s' % url for url in css]},
                           js=['schedule/js/%s' % url for url in js])

    '''
        列表页view
    '''

    def changelist_view(self, request, extra_context=None):
        courses = CourseContent.objects.all().order_by('id')
        extra_context = {
            'courses': courses
        }
        return super().changelist_view(request, extra_context)


