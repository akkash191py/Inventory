# Generated by Django 3.2.9 on 2022-01-20 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220115_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '2. Brands '},
        ),
        migrations.AlterModelOptions(
            name='brandlog',
            options={'verbose_name_plural': '8. Brand Log'},
        ),
        migrations.AlterModelOptions(
            name='categorylog',
            options={'verbose_name_plural': '7. Category Log'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('created_on',), 'verbose_name_plural': '6. Items '},
        ),
        migrations.AlterModelOptions(
            name='itemtype',
            options={'verbose_name_plural': '3. Item Type '},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': '1. Product Category'},
        ),
        migrations.AlterModelOptions(
            name='uom1',
            options={'verbose_name_plural': '4. Uom1'},
        ),
        migrations.AlterModelOptions(
            name='uom2',
            options={'verbose_name_plural': '5. Uom2'},
        ),
        migrations.CreateModel(
            name='ItemTypeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modify_by', models.CharField(blank=True, max_length=50, null=True)),
                ('modify_on', models.DateTimeField(auto_now=True)),
                ('details', models.CharField(max_length=200)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.itemtype')),
            ],
            options={
                'verbose_name_plural': '9. ItemType Log',
            },
        ),
    ]
