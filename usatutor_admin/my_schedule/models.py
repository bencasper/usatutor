from django.db import models


# Create your models here.
class UserTutorSchedule(models.Model):
    tutor_id = models.PositiveIntegerField(null=False)
    event_id = models.CharField(max_length=100, null=False)
    course_id = models.PositiveIntegerField(null=False)
    course_name = models.CharField(max_length=100, null=False)
    start_at = models.CharField(max_length=100, null=False)
    end_at = models.CharField(max_length=100, null=False)
    edit_by = models.CharField(max_length=100, null=False, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_tutor_schedule'
        verbose_name = "SCHEDULE"
        verbose_name_plural = "SCHEDULE"
