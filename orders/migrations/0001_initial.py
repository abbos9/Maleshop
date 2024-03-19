# Generated by Django 5.0.3 on 2024-03-19 15:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0022_productmodel_quantity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='total amount')),
                ('status_choices', models.CharField(choices=[('pending', 'Pending'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.productmodel')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.ordermodel')),
            ],
            options={
                'verbose_name': 'order item',
                'verbose_name_plural': 'order items',
            },
        ),
    ]
