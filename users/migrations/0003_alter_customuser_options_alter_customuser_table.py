# Generated by Django 5.0.1 on 2024-02-10 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_options_alter_customuser_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователи'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='Custom user',
        ),
    ]