# Generated by Django 4.1.4 on 2022-12-27 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("cart_id", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "shop_carts",
            },
        ),
    ]
