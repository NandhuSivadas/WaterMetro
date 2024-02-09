# Generated by Django 5.0 on 2024-01-18 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0011_tbl_stationmaster'),
        ('User', '0002_delete_ticketbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ticketbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Passenger_count', models.CharField(max_length=10)),
                ('book_amount', models.CharField(max_length=10)),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_tickettype')),
            ],
        ),
    ]
