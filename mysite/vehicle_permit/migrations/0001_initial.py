# Generated by Django 4.0.3 on 2022-05-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('CNIC', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='National ID Card Number')),
                ('full_name', models.CharField(max_length=60, verbose_name='Name of the Owner')),
                ('fhone_number', models.CharField(max_length=11)),
                ('citizen_of', models.CharField(max_length=6, verbose_name='select the Country')),
                ('address_of_owner', models.CharField(max_length=100)),
            ],
        ),
    ]