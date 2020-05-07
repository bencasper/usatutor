from django.db import models


class SaleOrder(models.Model):
    order_no = models.CharField(max_length=45, verbose_name='订单No')
    tutor_id = models.PositiveIntegerField()
    tutor_name = models.CharField(max_length=100)
    student_id = models.PositiveIntegerField()
    student_name = models.CharField(max_length=100)
    order_status = models.PositiveIntegerField()
    total_original_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_time = models.DateTimeField(blank=True, null=True)
    total_refundable_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_refunded_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_status = models.IntegerField()
    refund_apply_time = models.DateTimeField(blank=True, null=True)
    refunded_time = models.DateTimeField(blank=True, null=True)
    cancel_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'sale_order'
        verbose_name = "订单管理"
        verbose_name_plural = "订单管理"


class SaleOrderCourse(models.Model):
    course_id = models.PositiveIntegerField()
    course_name = models.CharField(max_length=100)
    course_level_id = models.PositiveIntegerField()
    course_level_name = models.CharField(max_length=45)
    course_begin_time = models.DateTimeField()
    couse_end_time = models.DateTimeField()
    couse_tutor_id = models.PositiveIntegerField()
    couse_tutor_name = models.CharField(max_length=100)
    couse_status = models.PositiveIntegerField()
    couse_income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    couse_refundable_amount = models.DecimalField(max_digits=10, decimal_places=2)
    couse_discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    couse_refunded_amount = models.DecimalField(max_digits=10, decimal_places=2)
    couse_refund_apply_time = models.DateTimeField(blank=True, null=True)
    couse_refunded_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'sale_order_course'


class SaleOrderFinance(models.Model):
    order_id = models.PositiveIntegerField()
    order_income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_income_ratio = models.DecimalField(max_digits=10, decimal_places=2)
    thirdparty_fee_radio = models.DecimalField(max_digits=10, decimal_places=2)
    ledger_type = models.IntegerField()
    ledger_day = models.IntegerField()
    self_income_amount = models.DecimalField(max_digits=10, decimal_places=2)
    partner_due = models.DecimalField(max_digits=10, decimal_places=2)
    thirdparty_fee = models.DecimalField(max_digits=10, decimal_places=2)
    ledger_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'sale_order_finance'


class SaleOrderPayment(models.Model):
    payment_type = models.PositiveIntegerField()
    payment_method_id = models.PositiveIntegerField()
    payment_method_name = models.CharField(max_length=100)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.PositiveIntegerField()
    thirdparty_payment_no = models.CharField(max_length=100)
    refunded = models.PositiveIntegerField()
    payment_apply_time = models.DateTimeField()
    payment_success_time = models.DateTimeField(blank=True, null=True)
    payment_failture_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'sale_order_payment'