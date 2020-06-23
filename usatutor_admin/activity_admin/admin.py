from django.contrib import admin

# Register your models here.
from middleware.admin import TutorREADAdmin

from .models import ActivityEntity


@admin.register(ActivityEntity)
class ActivityAdmin(TutorREADAdmin):
    pass
