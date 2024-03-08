# Generated by Django 5.0.1 on 2024-02-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_rename_image_1_postgallerymodel_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postgallerymodel',
            old_name='image',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='postgallerymodel',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='blog_detail'),
        ),
        migrations.AddField(
            model_name='postgallerymodel',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='blog_detail'),
        ),
        migrations.AddField(
            model_name='postgallerymodel',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='blog_detail'),
        ),
    ]
