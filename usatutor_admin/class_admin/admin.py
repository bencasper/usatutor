from django.contrib import admin

# Register your models here.
from middleware.admin import TutorREADAdmin

from class_admin.models import ClassAdminModel


@admin.register(ClassAdminModel)
class ClassAdmin(TutorREADAdmin):
    pass

