# Generated by Django 3.2.5 on 2023-03-16 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0012_auto_20230316_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='user',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='brand',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.brand'),
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 10, 24, 55, 619169, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 10, 24, 55, 632081, tzinfo=utc)),
        ),
    ]
