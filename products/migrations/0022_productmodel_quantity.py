# Generated by Django 5.0.1 on 2024-03-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_rename_cupinmodel_cupounmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
