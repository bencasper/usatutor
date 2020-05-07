# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class ActivityEntity(models.Model):
    tutor_id = models.PositiveIntegerField()
    tutor_name = models.CharField(max_length=100)
    student_id = models.PositiveIntegerField()
    student_name = models.CharField(max_length=100)
    order_id = models.PositiveIntegerField()
    course_id = models.PositiveIntegerField()
    course_name = models.CharField(max_length=100)
    due_begin_time = models.DateTimeField()
    due_end_time = models.DateTimeField()
    webrtc_id = models.CharField(max_length=100)
    real_begin_time = models.DateTimeField()
    real_end_time = models.DateTimeField(blank=True, null=True)
    real_duration = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    tutor_score = models.IntegerField()
    student_score = models.IntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'activity_entity'
        

class CourseContent(models.Model):
    level_id = models.PositiveIntegerField()
    course_name = models.CharField(max_length=100)
    course_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'course_content'


class CourseLevel(models.Model):
    level_name = models.CharField(max_length=100)
    level_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'course_level'


class SaleOrder(models.Model):
    order_no = models.CharField(max_length=45)
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


class TextbookCategory(models.Model):
    category_name = models.CharField(max_length=100)
    catetory_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'textbook_category'


class TextbookContent(models.Model):
    textbook_title = models.CharField(max_length=100)
    textbook_url = models.CharField(max_length=255)
    textbook_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'textbook_content'


class UserMemeberInfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_role_id = models.PositiveIntegerField()
    is_tutor = models.PositiveIntegerField()
    user_profile_url = models.CharField(max_length=255)
    user_wx_openid = models.CharField(max_length=100)
    user_wx_unionid = models.CharField(max_length=100)
    register_time = models.DateTimeField()
    user_introduce = models.CharField(max_length=255)
    is_active = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'user_memeber_info'


class UserRole(models.Model):
    role_name = models.CharField(max_length=100)
    role_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'user_role'


class UserTutorResume(models.Model):
    tutor_id = models.PositiveIntegerField()
    resume_item = models.CharField(max_length=255)
    resume_order = models.PositiveSmallIntegerField()
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'user_tutor_resume'


class UserTutorSchedule(models.Model):
    tutor_id = models.PositiveIntegerField()
    start_at = models.TimeField()
    end_at = models.TimeField()
    due_date = models.DateField()
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'user_tutor_schedule'
