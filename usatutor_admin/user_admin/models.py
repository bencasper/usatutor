from django.db import models
from django.forms import ModelForm

IS_TUTOR = (
    (0, 'NO'),
    (1, 'YES')
)

class UserMemeberInfo(models.Model):
    user_id = models.PositiveIntegerField(null=False)
    user_phone = models.CharField(max_length=20, null=False, default='')
    is_tutor = models.PositiveIntegerField(null=False, default=0)
    user_profile_url = models.CharField(max_length=255, null=False, default='')
    user_wx_openid = models.CharField(max_length=100, null=False, default='')
    user_wx_unionid = models.CharField(max_length=100, null=False, default='')
    register_time = models.DateTimeField(null=False)
    user_introduce = models.CharField(max_length=255, null=False, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_memeber_info'
        verbose_name = 'USER INFO'
        verbose_name_plural = 'USER INFO'


class UserTutorResume(models.Model):
    tutor_id = models.PositiveIntegerField()
    resume_item = models.CharField(max_length=255, null=False)
    resume_order = models.PositiveSmallIntegerField(null=False, default=1)
    edit_by = models.CharField(max_length=100, null=False, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_tutor_resume'
        verbose_name = 'USER RESUME'
        verbose_name_plural = 'USER RESUME'


class UserTutorSchedule(models.Model):
    tutor_id = models.PositiveIntegerField(null=False)
    course_id = models.PositiveIntegerField(null=False)
    course_name = models.CharField(max_length=100, null=False)
    start_at = models.TimeField(null=False)
    end_at = models.TimeField(null=False)
    due_date = models.DateField(null=False)
    edit_by = models.CharField(max_length=100, null=False, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_tutor_schedule'
        verbose_name = "SCHEDULE"
        verbose_name_plural = "SCHEDULE"
