# Generated by Django 5.0 on 2023-12-30 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]