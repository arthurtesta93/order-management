# Generated by Django 4.1.1 on 2022-09-14 20:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('kind', models.CharField(blank=True, choices=[('SELLER', 'Seller'), ('BUYER', 'Buyer'), ('SHIPPER', 'Shipper'), ('CONSIGNEE', 'Consignee'), ('CARRIER', 'Carrier'), ('TRANSPORT_MANAGER', 'Transport_manager'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=1024, verbose_name='Kind')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('kind', models.CharField(blank=True, choices=[('ORDER', 'Order'), ('ITEM', 'Item')], default='ORDER', max_length=1024, verbose_name='Kind')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
