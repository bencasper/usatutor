from django.contrib import admin

# Register your models here.
from .models import SaleOrder, SaleOrderCourse, SaleOrderPayment, SaleOrderFinance


@admin.register(SaleOrder, SaleOrderCourse, SaleOrderPayment, SaleOrderFinance)
class SaleAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    pass
