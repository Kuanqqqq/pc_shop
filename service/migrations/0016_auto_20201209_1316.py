# Generated by Django 3.1.3 on 2020-12-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_auto_20201209_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='orderitems',
            name='object_id',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='sold_product',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
