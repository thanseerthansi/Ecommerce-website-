# Generated by Django 4.1.2 on 2022-11-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0022_alter_productmodel_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='quanity_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]