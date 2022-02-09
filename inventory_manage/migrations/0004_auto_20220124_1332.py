# Generated by Django 3.2.9 on 2022-01-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_manage', '0003_remove_purchase_remaining_amt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': '3. Inventory'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default='0', null=True),
        ),
    ]