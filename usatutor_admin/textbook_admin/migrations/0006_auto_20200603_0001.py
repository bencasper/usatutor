# Generated by Django 2.2 on 2020-06-02 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook_admin', '0005_textbookcontent_cover_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textbookcontent',
            name='cover_img',
            field=models.URLField(default='', max_length=255),
        ),
    ]
