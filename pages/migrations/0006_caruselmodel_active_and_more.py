# Generated by Django 5.0.1 on 2024-01-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_blogmodel_phrase_creater_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='caruselmodel',
            name='active',
            field=models.BooleanField(blank=True, null=True, verbose_name=models.NullBooleanField(verbose_name='True')),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='phrase_creater_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='caruselmodel',
            name='image',
            field=models.ImageField(upload_to='Hero/'),
        ),
    ]
