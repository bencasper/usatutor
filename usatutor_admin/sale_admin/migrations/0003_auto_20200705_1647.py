# Generated by Django 2.2 on 2020-07-05 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale_admin', '0002_auto_20200624_0052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='saleorder',
            options={'verbose_name': 'Order Management', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='saleordercourse',
            options={'verbose_name': 'Order Course', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='saleorderfinance',
            options={'verbose_name': 'ORDER FINANCE', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='saleorderpayment',
            options={'verbose_name': 'ORDER PAYMENT', 'verbose_name_plural': ''},
        ),
    ]