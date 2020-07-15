from datetime import datetime, timedelta

import coreapi
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.filters import BaseFilterBackend

from rest_api.serializer import *


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TutorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    tutor列表
    """
    queryset = TutorInfo.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [permissions.AllowAny]


class ScheduleFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset

    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='tutor_id',
            location='query',
            required=True,
            type='string'
        ), ]


class TutorScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    tutor available schedule
    :parameter === tutor_id
    return 7天内排课
    """
    filter_backends = (ScheduleFilterBackend, )
    queryset = UserTutorSchedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tutor_id = self.request.query_params.get('tutor_id')
        today = datetime.utcnow().date()
        start = datetime(today.year, today.month, today.day)
        util = start + timedelta(8)
        return UserTutorSchedule.objects.filter(tutor_id=int(tutor_id))\
            .filter(start_at__gte=today).filter(start_at__lt=util)


class MyClassViewSet(viewsets.ModelViewSet):
    """
    选课、已选课列表
    """
    queryset = SaleOrderCourse.objects.all()
    serializer_class = OrderCourseSerializer
    permission_classes = [permissions.AllowAny]


class ClassRecordViewSet(viewsets.ReadOnlyModelViewSet):
    """
    已上课程列表
    """


class TextBookViewSet(viewsets.ReadOnlyModelViewSet):
    """
    课本相关
    """
    queryset = TextbookContent.objects.all()
    serializer_class = TextbookSerializer
    permission_classes = [permissions.AllowAny]