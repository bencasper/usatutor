from django import forms
from django.contrib import admin
from django.template.response import TemplateResponse

from .models import UserTutorSchedule


# Register your models here.
@admin.register(UserTutorSchedule)
class userScheduleAdmin(admin.ModelAdmin):
    change_list_template = "my_schedule/admin/my_schedule.html"

    @property
    def media(self):
        js = [
            'moment.min.js',
            'jquery.min.js',
            'jquery-ui.min.js',
            'fullcalendar.min.js',
            'scheduler.min.js',
        ]
        css = [
            'fullcalendar.min.css',
            'scheduler.min.css',
        ]
        return forms.Media(css={'all': ['useradmin/css/%s' % url for url in css]},
                           js=['useradmin/js/%s' % url for url in js])

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({

        })
        form_template = self.add_form_template
        request.current_app = self.admin_site.name

        return TemplateResponse(request, form_template, context)

