# Generated by Django 5.0.1 on 2024-01-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caruselmodel',
            name='imgage',
            field=models.ImageField(null=True, upload_to='Hero/'),
        ),
    ]