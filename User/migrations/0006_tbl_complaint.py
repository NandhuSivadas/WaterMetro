# Generated by Django 5.0 on 2024-02-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
