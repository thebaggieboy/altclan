# Generated by Django 3.2.5 on 2021-07-05 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_auto_20210704_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 14, 10, 11, 292543, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 14, 10, 11, 359005, tzinfo=utc)),
        ),
    ]
