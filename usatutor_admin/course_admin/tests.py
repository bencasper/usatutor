from django.test import TestCase

# Create your tests here.
from course_admin.models import CourseLevel


class CourseTestCase(TestCase):
    def setUp(self):
        CourseLevel.objects.create(level_name="basic", edit_by=1)
