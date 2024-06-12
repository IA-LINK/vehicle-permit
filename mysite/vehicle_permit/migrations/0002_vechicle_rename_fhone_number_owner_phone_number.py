# Generated by Django 4.0.3 on 2022-05-19 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_permit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vechicle',
            fields=[
                ('vehicle_name', models.CharField(max_length=30)),
                ('vehicle_number', models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='Vehicle Plate Number')),
                ('model', models.CharField(max_length=15, verbose_name='Vehicle Model')),
                ('chasis', models.CharField(max_length=20, verbose_name='Chasis Number')),
                ('engine', models.CharField(max_length=20, verbose_name='Engine Number')),
                ('vehicle_type', models.CharField(max_length=16, verbose_name='Type of Vehicle')),
            ],
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='fhone_number',
            new_name='phone_number',
        ),
    ]