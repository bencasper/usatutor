from django.contrib import admin

# Register your models here.
from student_admin.models import StudentInfo

from middleware.admin import TutorREADAdmin


@admin.register(StudentInfo)
class StudentAdmin(TutorREADAdmin):
    pass
