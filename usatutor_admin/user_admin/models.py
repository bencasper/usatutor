from django.db import models
from django.forms import ModelForm

IS_TUTOR = (
    (0, 'NO'),
    (1, 'YES')
)

USER_SEX = (
    (0, '女'),
    (1, '男')
)

# tutor
class TutorInfo(models.Model):
    user_id = models.PositiveIntegerField(null=False)
    user_phone = models.CharField(max_length=20, null=False, default='')
    user_name = models.CharField(max_length=100, null=False)
    user_age = models.IntegerField(null=False)
    user_sex = models.IntegerField(null=False, choices=USER_SEX, default=0)
    user_profile_url = models.CharField(max_length=255, null=False, default='')
    user_wx_openid = models.CharField(max_length=100, null=False, default='')
    user_wx_unionid = models.CharField(max_length=100, null=False, default='')
    has_license = models.BooleanField(null=False, default=False)
    user_strong_point = models.CharField(max_length=255, null=False, blank=True, default='')
    user_introduce = models.CharField(max_length=255, null=False, default='')
    min_student_age = models.IntegerField(null=False, blank=False, default=0)
    max_student_age = models.IntegerField(null=False, blank=False, default=0)
    my_videos_url = models.URLField(max_length=1000, null=True, blank=True, default='')
    class_record_url = models.URLField(max_length=1000, null=True, blank=True, default='')
    register_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_tutor_info'
        verbose_name = 'TUTOR INFO'
        verbose_name_plural = ''


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
        verbose_name_plural = ''


