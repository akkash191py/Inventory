# Generated by Django 3.2.9 on 2022-01-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220113_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uomlog',
            name='Uom1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UOM1', to='products.uom1'),
        ),
    ]
