# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import admin
from django.apps import apps


class MenuOrderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def order_app_list(self, app_list):
        ordered_app_list = []
        for app in app_list:
            app_config = apps.get_app_config(app['app_label'])
            if hasattr(app_config, 'order'):
                app['order'] = app_config.order
            else:
                app['order'] = 999
        ordered_app_list = sorted(app_list, key=lambda config: config['order'])
        return ordered_app_list

    def process_template_response(self, request, response):
        admin_index = admin.site.index(request)
        try:
            # try to get all installed models
            app_list = admin_index.context_data['app_list']
            self.app_list = self.order_app_list(app_list)

        except KeyError:
            # use app_list from context if this fails
            pass
        if hasattr(response, 'context_data') and response.context_data is not None:
            response.context_data['available_apps'] = None
            response.context_data['app_list'] = None
        return response
