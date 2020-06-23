from django.contrib import admin

from .models import UserTutorResume


@admin.register(UserTutorResume)
class userScheduleAdmin(admin.ModelAdmin):
    pass
