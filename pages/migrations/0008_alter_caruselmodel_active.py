# Generated by Django 5.0.1 on 2024-01-24 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_caruselmodel_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caruselmodel',
            name='active',
            field=models.BooleanField(),
        ),
    ]
