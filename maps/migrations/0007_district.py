# Generated by Django 3.2.9 on 2021-11-22 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_alter_address_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=10)),
                ('addr1', models.CharField(max_length=20)),
                ('addr2', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'district2',
                'managed': True,
            },
        ),
    ]