# Generated by Django 3.2.19 on 2023-07-31 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='label',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
