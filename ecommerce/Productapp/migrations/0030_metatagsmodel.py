# Generated by Django 4.1.2 on 2023-03-07 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0029_contactmodel_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetatagsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('tags', models.TextField(blank=True)),
            ],
        ),
    ]
