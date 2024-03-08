# Generated by Django 5.0.1 on 2024-02-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_postgallerymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='gallery',
            field=models.ManyToManyField(blank=True, null=True, to='products.postgallerymodel'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='material',
            field=models.TextField(blank=True, null=True),
        ),
    ]