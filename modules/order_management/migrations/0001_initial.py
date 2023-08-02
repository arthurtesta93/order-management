# Generated by Django 3.2.19 on 2023-07-31 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('kind', models.CharField(blank=True, choices=[('INBOUND', 'Inbound'), ('OUTBOUND', 'Outbound')], default='OUTBOUND', max_length=1024, verbose_name='Kind')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShippingOrder',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order_management.transaction')),
                ('facility_type', models.CharField(choices=[('STORAGE', 'Storage'), ('CORPORATE', 'Corporate Office'), ('WAREHOUSE', 'Warehouse'), ('FACILITY', 'Facility')], default='WAREHOUSE', max_length=10)),
                ('mode', models.CharField(choices=[('TL', 'Truck Load'), ('LTL', 'Less than Truck Load'), ('PTL', 'Partial Truck Load'), ('RAIL', 'Rail'), ('DRAYAGE', 'Drayage')], default=None, max_length=7, null=True)),
                ('date_received', models.DateTimeField(auto_now_add=True)),
                ('pickup_date', models.DateTimeField()),
                ('delivery_date', models.DateTimeField()),
                ('customer_reference', models.CharField(default='', max_length=128)),
                ('shipping_order_status', models.CharField(choices=[('EMPTY', 'Empty'), ('PROCESSED', 'Processed'), ('AWARDED', 'Awarded'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('POD_CONFIRMED', 'Proof Of Delivery Confirmed'), ('INVOICED', 'Invoiced')], default='EMPTY', max_length=14)),
                ('bill_to', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.organization')),
                ('carrier', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carrier', to='core.organization')),
                ('ship_from', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.facility')),
                ('ship_to', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.facility')),
            ],
            options={
                'abstract': False,
            },
            bases=('order_management.transaction',),
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('transaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='order_management.transaction')),
                ('purchase_order_status', models.CharField(choices=[('PLANNED', 'Planned'), ('PRODUCED', 'Processing'), ('PICKED', 'Packed'), ('PLACED', 'Placed')], default='PLANNED', max_length=9)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='core.organization')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller', to='core.organization')),
                ('shipping_order_id', models.ForeignKey(on_delete=models.SET('N/A'), to='order_management.shippingorder')),
            ],
            options={
                'abstract': False,
            },
            bases=('order_management.transaction',),
        ),
        migrations.CreateModel(
            name='ItemInstance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('quantity', models.IntegerField()),
                ('special_instructions', models.CharField(default=None, max_length=128, null=True)),
                ('item', models.ForeignKey(on_delete=models.SET('N/A'), related_name='item', to='core.item')),
                ('purchase_order_id', models.ForeignKey(on_delete=models.SET('N/A'), related_name='purchase-order+', to='order_management.purchaseorder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
