# -*- coding: utf-8 -*-
from django.urls import path

from my_schedule import views

urlpatterns = [
    path('schedule/list/<int:tutor_id>', views.schedule_list),
    path('schedule/<int:pk>/', views.schedule_detail),
]