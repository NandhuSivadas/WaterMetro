# Generated by Django 5.0 on 2023-12-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_stationmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_eventtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=10)),
            ],
        ),
    ]
