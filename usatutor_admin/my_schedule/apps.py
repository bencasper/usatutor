from django.apps import AppConfig


class MyScheduleConfig(AppConfig):
    name = 'my_schedule'
    verbose_name = 'My Schedule'
    order = 10