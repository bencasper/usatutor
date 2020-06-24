# Register your models here.
from course_admin.models import CourseContent
from django import forms
from django.contrib import admin
from django.template.response import TemplateResponse

from .models import UserTutorSchedule


@admin.register(UserTutorSchedule)
class UserScheduleAdmin(admin.ModelAdmin):
    change_list_template = "my_schedule/admin/my_schedule.html"

    def changelist_view(self, request, extra_context=None):
        courses = CourseContent.objects.all().order_by('id')
        extra_context = {
           'courses': courses
        }
        return super().changelist_view(request, extra_context)

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

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({

        })
        form_template = self.add_form_template
        request.current_app = self.admin_site.name

        return TemplateResponse(request, form_template, context)

