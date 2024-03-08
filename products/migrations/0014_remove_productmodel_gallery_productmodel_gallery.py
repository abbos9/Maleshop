# Generated by Django 5.0.1 on 2024-02-26 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_productmodel_gallery_productmodel_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='gallery',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.postgallerymodel'),
        ),
    ]