# Generated by Django 2.2 on 2020-07-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_admin', '0005_auto_20200705_1841'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='saleordercourse',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='saleordercourse',
            name='order_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
