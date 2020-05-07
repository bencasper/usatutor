from django.db import models


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