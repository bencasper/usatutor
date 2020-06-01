from django.core.management.base import BaseCommand
import unittest

from course_admin.models import CourseLevel


class Command(BaseCommand):
    help = """
    If you need Arguments, please check other modules in 
    django/core/management/commands.
    """

    def handle(self, **options):
        suite = unittest.TestLoader().loadTestsFromTestCase(TestChronology)
        unittest.TextTestRunner().run(suite)


class TestChronology(unittest.TestCase):
    def setUp(self):
        print("init course")

    def test_equality(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        CourseLevel.objects.create(level_name="basic", edit_by=1)



