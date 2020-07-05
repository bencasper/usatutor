from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from student_admin.models import StudentInfo

from middleware.admin import TutorREADAdmin, TutorCRUDAdmin


@admin.register(StudentInfo)
class StudentAdmin(TutorREADAdmin):
    list_display = ('id',
                    'user_name',
                    'user_age',
                    'user_phone',
                    'user_sex_tag',
                    'profile',
                    'wx_openid',
                    'total_course',
                    'done_course',
                    'ing_course',
                    )

    def profile(self, obj):
        return format_html('<img src="{}" width="100" height="80"/>'.format(obj.user_profile_url))
    profile.short_description = '照片'

    def user_sex_tag(self, obj):
        if obj.user_sex == 0:
            return '女'
        return '男'
    user_sex_tag.short_description = '性别'

    def wx_openid(self, obj):
        return obj.user_wx_openid + '(' + obj.user_wx_unionid + ')'
    wx_openid.short_description = '微信id'



