from django.apps import apps
from suit.templatetags.suit_menu import get_menu as origin_get_menu, register


@register.simple_tag(takes_context=True)
def get_menu(context, request):
    menu_manager = origin_get_menu(context, request)
    menu_manager.available_apps = order_app_list(menu_manager.available_apps)
    return menu_manager


def order_app_list(app_list):
    for app in app_list:
        app_config = apps.get_app_config(app['app_label'])
        if hasattr(app_config, 'order'):
            app['order'] = app_config.order
        else:
            app['order'] = 999
    ordered_app_list = sorted(app_list, key=lambda config: config['order'])
    return ordered_app_list