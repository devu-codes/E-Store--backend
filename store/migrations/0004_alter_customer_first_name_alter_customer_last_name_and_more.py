# Generated by Django 4.2.1 on 2023-05-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20230525_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
