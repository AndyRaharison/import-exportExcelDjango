# Generated by Django 5.0.1 on 2024-01-16 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tafika', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaire',
            name='date_naissance',
            field=models.CharField(max_length=25),
        ),
    ]
