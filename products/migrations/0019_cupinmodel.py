# Generated by Django 5.0.1 on 2024-03-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_remove_productmodel_gallery_productimagesmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CupinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=False)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'verbose_name': 'Cupon',
                'verbose_name_plural': 'Cupons',
            },
        ),
    ]