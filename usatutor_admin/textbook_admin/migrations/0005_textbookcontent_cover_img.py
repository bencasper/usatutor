# Generated by Django 2.2 on 2020-06-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook_admin', '0004_auto_20200602_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbookcontent',
            name='cover_img',
            field=models.ImageField(default='', max_length=255, upload_to=''),
        ),
    ]
