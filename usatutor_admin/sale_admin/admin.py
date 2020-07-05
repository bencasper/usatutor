from django.contrib import admin
from middleware.admin import TutorREADAdmin, TutorCRUDAdmin

# Register your models here.
from .models import SaleOrder, SaleOrderCourse, SaleOrderFinance

@admin.register(SaleOrder)
class SaleOrderAdmin(TutorREADAdmin):
    list_display = ('id',
                    'create_time',
                    'payment_method',
                    'thirdparty_paymentno',
                    'total_paid_amount',
                    'order_type_tag',
                    'order_type_id')

    def thirdparty_paymentno(self, obj):
        return '123'
    thirdparty_paymentno.short_description = '三方支付单号'

    def order_type_tag(self, obj):
        return '正教1课'
    order_type_tag.short_description = '购买类型'

    def order_type_id(self, obj):
        return obj.order_type
    order_type_id.short_description = '购买类型id'