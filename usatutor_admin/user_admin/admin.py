from django.contrib import admin
from django.contrib.auth import get_user

from .models import UserTutorResume
from middleware.admin import TutorCRUDAdmin


@admin.register(UserTutorResume)
class userScheduleAdmin(TutorCRUDAdmin):
    list_display = ('id', 'resume_item', 'edit_by')
    fields = ['resume_item', 'resume_order']

    def save_model(self, request, obj, form, change):
        obj.tutor_id = get_user(request).id
        obj.edit_by = get_user(request).username
        obj.save()
