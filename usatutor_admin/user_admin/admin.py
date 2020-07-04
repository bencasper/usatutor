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
                    'user_sex',
                    'user_strong_point',
                    'student_age_scope',
                    'has_license',
                    'profile',
                    'my_videos_url',
                    'records')

    def profile(self, obj):
        return format_html('<img src="{}" width="100" height="80"/>'.format(obj.cover_img))
    profile.short_descption = '照片'

    def has_license(self, obj):
        if obj.has_license:
            return '有'
        return '无'
    has_license.short_description = '有无教师证'

    def student_age_scope(self, obj):
        if obj.min_student_age is not None and obj.max_student_age is not None:
            return obj.min_student_age + ' ~ ' + obj.max_student_age
    student_age_scope.short_description = '可教年龄'

    def records(self, obj):
        return ''
    records.short_description = '上课记录'

    def my_videos_url(self, obj):
        return format_html('<a href="{}"/>查看</a>'.format(obj.cover_img))

    def user_strong_point(self, obj):
        return obj.user_strong_point
    user_strong_point.short_description = '特长'
