# Generated by Django 3.1.3 on 2020-11-26 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_purchase_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='quantity',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]