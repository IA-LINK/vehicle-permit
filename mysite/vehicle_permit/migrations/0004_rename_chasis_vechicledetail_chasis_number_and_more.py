# Generated by Django 4.0.3 on 2022-06-24 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_permit', '0003_vechicledetail_delete_vechicle_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vechicledetail',
            old_name='chasis',
            new_name='chasis_number',
        ),
        migrations.RenameField(
            model_name='vechicledetail',
            old_name='engine',
            new_name='engine_number',
        ),
        migrations.RenameField(
            model_name='vechicledetail',
            old_name='model',
            new_name='model_number',
        ),
    ]