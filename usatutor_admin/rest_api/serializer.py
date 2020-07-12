# -*- coding: utf-8 -*-
# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets

from my_schedule.models import UserTutorSchedule
from sale_admin.models import SaleOrderCourse
from textbook_admin.models import TextbookContent
from user_admin.models import TutorInfo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TutorInfo
        fields = ['id', 'user_name', 'user_sex', 'user_profile_url', 'has_license', 'user_strong_point', 'user_introduce', 'min_student_age', 'max_student_age']


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTutorSchedule
        fields = ['id', 'tutor_id', 'course_id', 'course_name', 'start_at', 'end_at']


class OrderCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SaleOrderCourse
        fields = ['order_id',
                  'id',
                  'course_tutor_id',
                  'course_tutor_name',
                  'course_student_id',
                  'course_student_name',
                  'course_status',
                  'create_time']


class TextbookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextbookContent
        fields = [
            'id',
            'unit',
            'unit_title',
            'textbook_title',
            'grammar',
            'cover_img',
            'textbook_url',
            'textbook_desc',
        ]
