# Generated by Django 5.0.1 on 2024-01-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='categories',
            table='Cat',
        ),
    ]
