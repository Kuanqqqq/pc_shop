# Generated by Django 3.1.3 on 2020-12-04 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20201204_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu_cooler',
            old_name='cooler',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='gpu',
            old_name='gpu',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='memory',
            old_name='memory',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherboard',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power',
            new_name='name',
        ),
    ]
