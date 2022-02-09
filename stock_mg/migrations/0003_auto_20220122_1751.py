# Generated by Django 3.2.9 on 2022-01-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_mg', '0002_auto_20220120_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockissue',
            name='issue_no',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Issue no'),
        ),
        migrations.AlterField(
            model_name='stockreceive',
            name='batch_no',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Batch no'),
        ),
    ]