# Generated by Django 5.0.1 on 2024-01-23 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_caruselmodel_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caruselmodel',
            name='active',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
