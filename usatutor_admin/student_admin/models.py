from django.db import models


# Create your models here.

# tutor
class StudentInfo(models.Model):
    user_id = models.PositiveIntegerField(null=False)
    user_phone = models.CharField(max_length=20, null=False, default='', verbose_name='电话')
    user_name = models.CharField(max_length=100, null=False, verbose_name='姓名')
    user_age = models.IntegerField(null=False, verbose_name='年龄')
    user_sex = models.IntegerField(null=False, verbose_name='性别')
    user_profile_url = models.CharField(max_length=255, null=False, default='', verbose_name='照片')
    user_wx_openid = models.CharField(max_length=100, null=False, default='')
    user_wx_unionid = models.CharField(max_length=100, null=False, default='')
    total_course = models.IntegerField(default=0, verbose_name='总课程数')
    ing_course = models.IntegerField(default=0, verbose_name='已上')
    done_course = models.IntegerField(default=0, verbose_name='未上')
    register_time = models.DateTimeField(null=False)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_student_info'
        verbose_name = 'STUDENT INFO'
        verbose_name_plural = 'STUDENT INFO'
