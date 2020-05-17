from django.contrib import admin

# Register your models here.
from .models import UserTutorSchedule


@admin.register(UserTutorSchedule)
class userScheduleAdmin(admin.ModelAdmin):
    add_form_template = "user_admin/admin/my_schedule.html"
    pass
