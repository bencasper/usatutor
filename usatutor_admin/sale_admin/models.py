from django.db import models

# 订单状态 1:待付款 2:已付款 3:已取消 4:履约中 5:履约完成
ORDER_STATUS = (
    (1, '代付款'),
    (2, '已取消'),
    (3, '已付款'),
    (4, '履约中'),
    (5, '履约完成'),
    (6, '售后中'),
    (7, '售后完成')
)

# 退款状态
REFUND_STATUS = (
    (0, '不可退款'),
    (1, '可退款'),
    (2, '退款中'),
    (3, '部分退款成功'),
    (4, '全额退款')
)

class SaleOrder(models.Model):
    order_no = models.CharField(max_length=45, null=False)
    tutor_id = models.PositiveIntegerField(null=False)
    tutor_name = models.CharField(max_length=100, null=False)
    student_id = models.PositiveIntegerField(null=False)
    student_name = models.CharField(max_length=100, null=False)
    order_status = models.PositiveIntegerField(null=False, default=1)
    total_original_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    total_due_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    total_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_time = models.DateTimeField(blank=True, null=True)
    total_refundable_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    total_refunded_amount = models.DecimalField(max_digits=10, decimal_places=2,  null=False, default=0.00)
    refund_status = models.IntegerField(blank=False, default=0)
    refund_apply_time = models.DateTimeField(blank=True, null=True)
    refunded_time = models.DateTimeField(blank=True, null=True)
    cancel_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sale_order'
        verbose_name = "Order Management"
        verbose_name_plural = ""

# 课程状态 1 未授课 2 已授课 3 已退课
COURSE_STATUS = (
    (1, '未授课'),
    (2, '已授课'),
    (3, '已退课'),
)

class SaleOrderCourse(models.Model):
    course_name = models.CharField(max_length=100, null=False)
    course_level_id = models.PositiveIntegerField(null=False)
    course_level_name = models.CharField(max_length=45, null=False)
    course_begin_time = models.DateTimeField(null=False)
    course_end_time = models.DateTimeField(null=False)
    course_tutor_id = models.PositiveIntegerField(null=False)
    course_tutor_name = models.CharField(max_length=100, null=False)
    course_status = models.PositiveIntegerField(null=False, default=1)
    course_income_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    course_refundable_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    course_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    course_refunded_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    course_refund_apply_time = models.DateTimeField(blank=True, null=True)
    course_refunded_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sale_order_course'
        verbose_name = 'Order Course'
        verbose_name_plural = ''


# 分账类型 1 订单履约结束后 t+
LEDGER_TYPE = (
    (1, 'T+')
)

class SaleOrderFinance(models.Model):
    order_id = models.PositiveIntegerField(null=False)
    order_income_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    order_income_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    thirdparty_fee_radio = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    ledger_type = models.IntegerField(null=False, default=1)
    ledger_day = models.IntegerField(null=False, default=1)
    self_income_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    partner_due = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    thirdparty_fee = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    ledger_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sale_order_finance'
        verbose_name = 'ORDER FINANCE'
        verbose_name_plural = ''

#支付类型 1 支付 2 退款
PAYMENT_TYPE = (
    (1, '支付'),
    (2, '退款'),
)

#支付方式 1 微信 2 支付宝
PAYMENT_METHOD = (
    (1, '微信'),
    (2, '支付宝'),
)

#支付状态  1 未支付 2 已支付 3 支付失败 4 退款中 5退款完成 6 退款失败
PAYMENT_STATUS = (
    (1, '未支付'),
    (2, '已支付'),
    (3, '支付失败'),
    (4, '退款中'),
    (5, '退款完成'),
    (6, '退款失败')
)

class SaleOrderPayment(models.Model):
    payment_type = models.PositiveIntegerField(null=False, default=1)
    payment_method_id = models.PositiveIntegerField(null=False)
    payment_method_name = models.CharField(max_length=100, null=False)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    payment_status = models.PositiveIntegerField(null=False, default=1)
    thirdparty_payment_no = models.CharField(max_length=100, null=False)
    payment_apply_time = models.DateTimeField(null=False)
    payment_success_time = models.DateTimeField(blank=True, null=True)
    payment_failture_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sale_order_payment'
        verbose_name = 'ORDER PAYMENT'
        verbose_name_plural = ''