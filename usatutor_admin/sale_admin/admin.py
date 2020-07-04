from django.contrib import admin
from middleware.admin import TutorREADAdmin

# Register your models here.
from .models import SaleOrder, SaleOrderCourse, SaleOrderFinance

@admin.register(SaleOrder)
class SaleOrderAdmin(TutorREADAdmin):
    pass

