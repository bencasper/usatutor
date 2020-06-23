from django.db import models


class CourseContent(models.Model):
    course_name = models.CharField(max_length=100, null=False, blank=False)
    course_desc = models.CharField(max_length=255, null=False, default='')
    edit_by = models.CharField(max_length=100, null=False, blank=True, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_content'
        verbose_name = 'Course'
        verbose_name_plural = 'COURSE'


class CourseLevel(models.Model):
    level_name = models.CharField(max_length=100, null=False, blank=False)
    level_desc = models.CharField(max_length=255, null=False, blank=False)
    edit_by = models.CharField(max_length=100, null=False, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'course_level'
        verbose_name = 'Course Level'
        verbose_name_plural = 'Course Levels'