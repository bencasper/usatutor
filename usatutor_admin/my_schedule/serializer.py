# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import UserTutorSchedule


class TutorScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTutorSchedule
        fields = ['tutor_id', 'course_id', 'course_name', 'start_at', 'end_at', 'due_date', 'edit_by' ]
