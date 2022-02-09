# Generated by Django 3.2.9 on 2022-02-08 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0002_auto_20220127_1804'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0011_alter_multiimage_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Purchase Title')),
                ('prefix', models.CharField(default='PO-', max_length=20)),
                ('po_no', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True, verbose_name='Purchase Number')),
                ('orderstatus', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100, verbose_name='OrderStatus')),
                ('created_date', models.DateTimeField(auto_now=True, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.vendor')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Orders',
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('status', models.CharField(max_length=30, verbose_name='Item status')),
                ('created_date', models.DateTimeField(auto_now=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.item')),
                ('po', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.purchaseorder')),
            ],
            options={
                'verbose_name': 'Purchase Item',
                'verbose_name_plural': 'Add Purchase Item',
            },
        ),
    ]
