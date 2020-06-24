# -*- coding: utf-8 -*-
from django.contrib.admin import AdminSite
from django.http import HttpResponseRedirect


class TutorSite(AdminSite):

    def index(self, request, extra_context=None):
        return HttpResponseRedirect("my_schedule/usertutorschedule/")


