# Generated by Django 5.0 on 2023-12-30 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=10)),
            ],
        ),
    ]
