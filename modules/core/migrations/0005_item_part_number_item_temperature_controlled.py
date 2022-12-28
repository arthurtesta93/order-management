# Generated by Django 4.1.4 on 2022-12-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_item_hazardous'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='part_number',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='temperature_controlled',
            field=models.BooleanField(default=False),
        ),
    ]
