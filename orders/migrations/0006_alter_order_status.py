# Generated by Django 5.0.8 on 2024-08-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='New', max_length=10),
        ),
    ]
