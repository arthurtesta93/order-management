# Generated by Django 3.2.2 on 2023-01-23 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20230119_1809'),
        ('order_management', '0007_auto_20230123_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingorder',
            name='bill_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='core.organization'),
        ),
        migrations.AddField(
            model_name='shippingorder',
            name='ship_to',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='order_management.facilitystop'),
        ),
    ]