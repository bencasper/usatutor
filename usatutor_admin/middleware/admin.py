from django.contrib import admin
from django.contrib.auth import get_user


class TemplateAdmin(admin.ModelAdmin):
    pass


class TutorCRUDAdmin(TemplateAdmin):

    def save_model(self, request, obj, form, change):
        obj.edit_by = get_user(request).username
        obj.save()

    def _get_base_actions(self):
        return []


class TutorREADAdmin(TemplateAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def _get_base_actions(self):
        return []
