# Generated by Django 5.1 on 2024-08-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_variation_variation_stock_alter_product_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100),
        ),
    ]
