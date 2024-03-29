# Generated by Django 5.0 on 2024-02-08 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_initial'),
        ('User', '0009_delete_tbl_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
                ('reply', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
