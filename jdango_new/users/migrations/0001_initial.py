# Generated by Django 4.1.3 on 2022-11-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('rank', models.IntegerField()),
                ('point', models.TextField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
