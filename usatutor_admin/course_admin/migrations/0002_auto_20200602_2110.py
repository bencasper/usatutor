# Generated by Django 2.2 on 2020-06-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='edit_by',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='courselevel',
            name='edit_by',
            field=models.CharField(default='', max_length=100),
        ),
    ]