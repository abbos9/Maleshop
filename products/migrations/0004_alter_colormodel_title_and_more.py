# Generated by Django 5.0.1 on 2024-01-28 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_subcategorymodel_productmodel_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colormodel',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategorymodel'),
        ),
        migrations.AlterField(
            model_name='subcategorymodel',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
