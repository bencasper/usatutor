# Generated by Django 2.2 on 2020-05-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMemeberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('user_phone', models.CharField(default='', max_length=20)),
                ('is_tutor', models.PositiveIntegerField(default=0)),
                ('user_profile_url', models.CharField(default='', max_length=255)),
                ('user_wx_openid', models.CharField(default='', max_length=100)),
                ('user_wx_unionid', models.CharField(default='', max_length=100)),
                ('register_time', models.DateTimeField()),
                ('user_introduce', models.CharField(default='', max_length=255)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'USER INFO',
                'verbose_name_plural': 'USER INFO',
                'db_table': 'user_memeber_info',
            },
        ),
        migrations.CreateModel(
            name='UserTutorResume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_id', models.PositiveIntegerField()),
                ('resume_item', models.CharField(max_length=255)),
                ('resume_order', models.PositiveSmallIntegerField(default=1)),
                ('edit_by', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'USER RESUME',
                'verbose_name_plural': 'USER RESUME',
                'db_table': 'user_tutor_resume',
            },
        ),
        migrations.CreateModel(
            name='UserTutorSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_id', models.PositiveIntegerField()),
                ('course_id', models.PositiveIntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('start_at', models.TimeField()),
                ('end_at', models.TimeField()),
                ('due_date', models.DateField()),
                ('edit_by', models.PositiveIntegerField()),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'SCHEDULE',
                'verbose_name_plural': 'SCHEDULE',
                'db_table': 'user_tutor_schedule',
            },
        ),
    ]
