# Generated by Django 3.2.9 on 2022-01-15 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_uomlog_uom1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Item name')),
                ('code_type', models.CharField(choices=[('Item KEY', 'Item Key'), ('ID', 'ID')], max_length=30, verbose_name='Code Type')),
                ('sku', models.CharField(help_text='Enter Product Stock Keeping Unit', max_length=13, unique=True, verbose_name='SKU')),
                ('barcode', models.CharField(help_text='Enter Product Barcode (ISBN, UPC ...)', max_length=13, unique=True)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('short_details', models.TextField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold'), ('Restocking', 'Restocking'), ('NotAvailable', 'Not Available')], default='Available', max_length=50)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory')),
                ('item_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Itemtype', to='products.itemtype')),
                ('uom1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.uom1')),
                ('uom2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.uom2')),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.AlterModelOptions(
            name='uomlog',
            options={'verbose_name_plural': 'Uom Log'},
        ),
        migrations.CreateModel(
            name='ItemLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.CharField(help_text='Enter Product Stock Keeping Unit', max_length=13, verbose_name='item code')),
                ('modify_by', models.CharField(blank=True, max_length=50, null=True)),
                ('modify_on', models.DateTimeField(auto_now=True)),
                ('details', models.CharField(max_length=500)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.item')),
            ],
            options={
                'verbose_name_plural': 'Item Log',
            },
        ),
    ]
