# Generated by Django 3.2.2 on 2023-01-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20230111_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default=None, max_length=30, verbose_name='First Name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=None, max_length=30, verbose_name='Last Name'),
        ),
        migrations.AddField(
            model_name='contact',
            name='observations',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=None, max_length=40, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=None, max_length=20, verbose_name='Phone'),
        ),
    ]
