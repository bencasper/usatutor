from suit.apps import DjangoSuitConfig
from django.contrib.admin.apps import AdminConfig


class SuitConfig(DjangoSuitConfig):
    # name = 'usa_tutor'
    # verbose_name = '北美外教'

    # Menu and header layout - horizontal or vertical
    layout = 'horizontal'

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True
