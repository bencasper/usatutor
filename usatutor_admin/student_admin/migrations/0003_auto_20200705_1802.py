# Generated by Django 2.2 on 2020-07-05 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_admin', '0002_auto_20200705_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='done_course',
            field=models.IntegerField(default=0, verbose_name='已上'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='ing_course',
            field=models.IntegerField(default=0, verbose_name='未上'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='user_sex',
            field=models.IntegerField(choices=[(0, '女'), (1, '男')], verbose_name='性别'),
        ),
    ]
