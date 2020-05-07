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