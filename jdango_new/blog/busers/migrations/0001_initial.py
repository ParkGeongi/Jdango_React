# Generated by Django 4.1.4 on 2022-12-27 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Buser",
            fields=[
                ("blog_userid", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.TextField()),
                ("nickname", models.TextField()),
                ("password", models.TextField()),
            ],
            options={
                "db_table": "blog_busers",
            },
        ),
    ]
