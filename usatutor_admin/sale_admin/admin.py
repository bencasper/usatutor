from django.contrib import admin

# Register your models here.
from .models import SaleOrder, SaleOrderCourse, SaleOrderPayment, SaleOrderFinance

admin.site.register(SaleOrder)
admin.site.register(SaleOrderPayment)

