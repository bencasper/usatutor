from django.contrib import admin
from django.contrib.auth import get_user
from django.utils.html import format_html

from .models import UserTutorResume, TutorInfo
from middleware.admin import TutorREADAdmin

@admin.register(TutorInfo)
class TutorAdmin(TutorREADAdmin):
    list_display = ('id',
                    'user_name',
                    'user_age',
                    'user_sex_tag',
                    'user_strong_point_tag',
                    'student_age_scope',
                    'has_license',
                    'profile',
                    'my_videos',
                    'class_record')

    def profile(self, obj):
        return format_html('<img src="{}" width="100" height="80"/>'.format(obj.user_profile_url))
    profile.short_description = '照片'

    def user_sex_tag(self, obj):
        if obj.user_sex == 0:
            return '女'
        return '男'
    user_sex_tag.short_description = '性别'

    def student_age_scope(self, obj):
        if obj.min_student_age is not None and obj.max_student_age is not None:
            return str(obj.min_student_age) + ' ~ ' + str(obj.max_student_age)
    student_age_scope.short_description = '可教年龄'

    def class_record(self, obj):
        return format_html('<a href="{}"/>查看</a>'.format(obj.class_record_url))
    class_record.short_description = '上课记录'

    def my_videos(self, obj):
        return format_html('<a href="{}"/>查看</a>'.format(obj.user_profile_url))

    def user_strong_point_tag(self, obj):
        return obj.user_strong_point
    user_strong_point_tag.short_description = '特长'
