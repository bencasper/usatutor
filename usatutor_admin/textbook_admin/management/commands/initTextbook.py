from django.core.management.base import BaseCommand
from xlrd import open_workbook
import unittest
import os



class Command(BaseCommand):
    help = """
    If you need Arguments, please check other modules in 
    django/core/management/commands.
    """

    def handle(self, **options):
        suite = unittest.TestLoader().loadTestsFromTestCase(ImportTextbookFromExcel)
        unittest.TextTestRunner().run(suite)


class ImportTextbookFromExcel(unittest.TestCase):
    def setUp(self):
        print("init course")

    def test_equality(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        script_path = os.path.dirname(__file__)
        excel_path = os.path.join(script_path, '../../usatutor_textbook.xlsx')
        wb = open_workbook(excel_path)
        sheet = wb.sheet_by_index(0)
        print(sheet.nrows, sheet.ncols)








