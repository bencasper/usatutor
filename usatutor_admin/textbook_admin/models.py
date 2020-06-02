from django.db import models


class TextbookContent(models.Model):
    # level_id 暂时不用
    level_id = models.PositiveIntegerField(null=True, blank=True)
    level_name = models.CharField(max_length=100, null=False, default='')
    unit = models.CharField(max_length=100, null=False)
    unit_title = models.CharField(max_length=255, null=False)
    textbook_title = models.CharField(max_length=100, null=False)
    grammar = models.CharField(max_length=100, null=False, default='')
    cover_img = models.ImageField(max_length=255, null=False, default='')
    textbook_url = models.URLField(max_length=255, null=False, default='')
    textbook_desc = models.CharField(max_length=255, null=False, default='')
    tag = models.CharField(max_length=255, null=False, default='')
    edit_by = models.CharField(max_length=100, null=False, default='')
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'textbook_content'
        verbose_name = 'TEXTBOOK'
        verbose_name_plural = 'TEXTBOOKS'

    def __str__(self):
        return "%s" % self.textbook_title


