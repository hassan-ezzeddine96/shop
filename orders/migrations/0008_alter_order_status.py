# Generated by Django 5.0.8 on 2024-08-14 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('New', 'New'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=10),
        ),
    ]
