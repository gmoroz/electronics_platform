# Generated by Django 4.1.5 on 2023-01-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_remove_distributor_contacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessman',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='retailchain',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
