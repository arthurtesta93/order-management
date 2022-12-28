# Generated by Django 4.1.4 on 2022-12-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='kind',
            field=models.CharField(blank=True, choices=[('INBOUND', 'Inbound'), ('OUTBOUND', 'Outbound')], default='OUTBOUND', max_length=1024, verbose_name='Kind'),
        ),
    ]