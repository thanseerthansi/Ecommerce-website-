# Generated by Django 4.1.2 on 2022-10-10 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0002_categorymodel_citymodel_imagemodel_ordermodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingorderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=200)),
                ('contact', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Productapp.productmodel')),
            ],
        ),
    ]
