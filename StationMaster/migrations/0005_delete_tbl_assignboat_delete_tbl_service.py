# Generated by Django 5.1.6 on 2025-03-28 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StationMaster', '0004_tbl_assignboat'),
        ('User', '0023_remove_tbl_ticketbooking_assign_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_assignboat',
        ),
        migrations.DeleteModel(
            name='tbl_service',
        ),
    ]
