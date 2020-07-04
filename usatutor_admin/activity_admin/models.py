from django.db import models

ACTIVITY_STATUS = (
    (0, '未开始'),
    (1, '授课中'),
    (2, '授课中断'),
    (3, '授课完成'),
)

class ActivityEntity(models.Model):
    tutor_id = models.PositiveIntegerField(null=False)
    tutor_name = models.CharField(max_length=100, null=False)
    student_id = models.PositiveIntegerField(null=False)
    student_name = models.CharField(max_length=100, null=False)
    order_id = models.PositiveIntegerField(null=False)
    course_id = models.PositiveIntegerField(null=False)
    course_name = models.CharField(max_length=100, null=False)
    due_begin_time = models.DateTimeField(null=False)
    due_end_time = models.DateTimeField(null=False)
    webrtc_id = models.CharField(max_length=100, null=False, default='')
    real_begin_time = models.DateTimeField(blank=True, null=True)
    real_end_time = models.DateTimeField(blank=True, null=True)
    real_duration = models.PositiveIntegerField(null=False, default=0)
    status = models.PositiveIntegerField(null=False, default=0)
    tutor_score = models.IntegerField(null=False, default=10)
    student_score = models.IntegerField(null=False, default=10)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activity_entity'
        verbose_name = 'activity'
        verbose_name_plural = ''
