# Generated by Django 2.2 on 2020-06-23 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleorder',
            options={'verbose_name': 'Order Management', 'verbose_name_plural': 'ORDER MANAGEMENT'},
        ),
        migrations.AlterModelOptions(
            name='saleordercourse',
            options={'verbose_name': 'Order Course', 'verbose_name_plural': 'ORDER COURSE'},
        ),
    ]
