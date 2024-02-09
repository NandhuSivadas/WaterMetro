# Generated by Django 5.0 on 2024-01-19 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_tbl_stationmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_addevent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addevent_title', models.CharField(max_length=50)),
                ('addevent_details', models.CharField(max_length=50)),
                ('addevent_passengercount', models.IntegerField()),
                ('addevent_eventtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_eventtype')),
            ],
        ),
    ]