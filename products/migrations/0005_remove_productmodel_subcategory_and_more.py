# Generated by Django 5.0.1 on 2024-01-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_colormodel_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='subcategory',
            field=models.ManyToManyField(to='products.subcategorymodel'),
        ),
    ]