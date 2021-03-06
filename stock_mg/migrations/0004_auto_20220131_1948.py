# Generated by Django 3.2.9 on 2022-01-31 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_multiimage_options'),
        ('stock_mg', '0003_auto_20220122_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='totalinstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
            options={
                'verbose_name_plural': ' Total Received',
            },
        ),
        migrations.CreateModel(
            name='totaloutstock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
            options={
                'verbose_name_plural': 'Total Issued',
            },
        ),
        migrations.DeleteModel(
            name='StockRecord',
        ),
        migrations.AddField(
            model_name='stockissue',
            name='stock_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock_mg.totalinstock'),
        ),
        migrations.AddField(
            model_name='stockreceive',
            name='stock_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock_mg.totalinstock'),
        ),
    ]
