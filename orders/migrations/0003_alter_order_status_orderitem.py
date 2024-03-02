# Generated by Django 5.0.1 on 2024-03-02 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('orders', '0002_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('in process', 'В обработке'), ('delivered', 'Доставлен')], default=None, max_length=20),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.products', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Проданный товар',
                'verbose_name_plural': 'Проданные товары',
                'db_table': 'order_item',
            },
        ),
    ]