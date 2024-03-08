# Generated by Django 5.0.1 on 2024-02-17 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_messagemodel_options_messagemodel_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='blogs.postmodel'),
        ),
    ]
