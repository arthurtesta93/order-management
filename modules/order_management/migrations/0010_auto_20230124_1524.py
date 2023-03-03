# Generated by Django 3.2.2 on 2023-01-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0009_auto_20230124_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingorder',
            name='last_update',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='purchase_order_status',
            field=models.CharField(choices=[('PLANNED', 'Planned'), ('PRODUCED', 'Processing'), ('PICKED', 'Packed'), ('PLACED', 'Placed')], default='PLANNED', max_length=9),
        ),
        migrations.AddField(
            model_name='shippingorder',
            name='shipping_order_status',
            field=models.CharField(choices=[('EMPTY', 'Empty'), ('PROCESSED', 'Processed'), ('AWARDED', 'Awarded'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('POD_CONFIRMED', 'Proof Of Delivery Confirmed'), ('INVOICED', 'Invoiced')], default='EMPTY', max_length=14),
        ),
    ]