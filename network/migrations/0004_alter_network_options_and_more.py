# Generated by Django 4.1.5 on 2023-01-19 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_rename_factory_network_plant'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='network',
            options={'verbose_name': 'Сеть поставщиков', 'verbose_name_plural': 'Сети поставщиков'},
        ),
        migrations.RenameField(
            model_name='network',
            old_name='business_man',
            new_name='businessman',
        ),
    ]
