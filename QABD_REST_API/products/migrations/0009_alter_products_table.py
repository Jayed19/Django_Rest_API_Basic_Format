# Generated by Django 4.1.4 on 2022-12-24 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_rename_status_products_status"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="products",
            table="product",
        ),
    ]
