# Generated by Django 3.2.9 on 2022-02-07 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_mg', '0005_alter_stockissue_stock_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='totalinstock',
            options={'verbose_name_plural': ' 3. Total Received'},
        ),
        migrations.AlterModelOptions(
            name='totaloutstock',
            options={'verbose_name_plural': '4. Total Issued'},
        ),
    ]