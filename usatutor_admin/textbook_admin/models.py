from django.db import models


class TextbookCategory(models.Model):
    category_name = models.CharField(max_length=100)
    catetory_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'textbook_category'


class TextbookContent(models.Model):
    textbook_title = models.CharField(max_length=100)
    textbook_url = models.CharField(max_length=255)
    textbook_desc = models.CharField(max_length=255)
    edit_by = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    create_time = models.DateTimeField()

    class Meta:
        db_table = 'textbook_content'
