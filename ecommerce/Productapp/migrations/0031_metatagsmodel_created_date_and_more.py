# Generated by Django 4.1.2 on 2023-03-07 07:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0030_metatagsmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='metatagsmodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metatagsmodel',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
