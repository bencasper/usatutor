from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

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


class TutorScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    tutor available schedule
    """
    queryset = UserTutorSchedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.AllowAny]


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