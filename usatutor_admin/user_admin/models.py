from django.db import models


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
