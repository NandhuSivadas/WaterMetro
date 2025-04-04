# Generated by Django 5.1.6 on 2025-03-24 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0020_tbl_addevent'),
        ('Guest', '0003_initial'),
        ('StationMaster', '0004_tbl_assignboat'),
        ('User', '0021_delete_tbl_ticketbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ticketbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('Passenger_count', models.CharField(max_length=10)),
                ('book_amount', models.CharField(max_length=10)),
                ('status', models.IntegerField(default=0)),
                ('assign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StationMaster.tbl_assignboat')),
                ('service_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_from', to='StationMaster.tbl_service')),
                ('service_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_to', to='StationMaster.tbl_service')),
                ('ticket_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_tickettype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
