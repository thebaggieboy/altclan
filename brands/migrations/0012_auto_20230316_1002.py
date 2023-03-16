# Generated by Django 3.2.5 on 2023-03-16 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0011_auto_20230316_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchandise',
            old_name='merchandise_image',
            new_name='display_image',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='images',
            field=models.ManyToManyField(to='brands.MerchandiseGallery'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 10, 2, 3, 537606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='labels',
            field=models.CharField(choices=[('None', 'None'), ('New Merchandise', 'New Merchandise'), ('Limited Stock', 'Limited Stock'), ('FREE DELIVERY', 'FREE DELIVERY')], default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchandisegallery',
            name='image_5',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Merch Image'),
        ),
        migrations.AlterField(
            model_name='merchandisegallery',
            name='image_6',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Merch Image'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 10, 2, 3, 546714, tzinfo=utc)),
        ),
    ]