# Generated by Django 3.1.3 on 2020-11-27 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20201126_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
