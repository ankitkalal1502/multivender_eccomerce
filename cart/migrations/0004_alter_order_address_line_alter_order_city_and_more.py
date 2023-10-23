# Generated by Django 4.2.6 on 2023-10-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_address_line_order_city_order_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address_line',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=255),
        ),
    ]
