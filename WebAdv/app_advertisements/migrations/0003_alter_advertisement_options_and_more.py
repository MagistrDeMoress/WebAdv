# Generated by Django 4.2.3 on 2023-07-27 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_alter_advertisement_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={},
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='Advertisement',
        ),
    ]
