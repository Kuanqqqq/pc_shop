# Generated by Django 3.1.3 on 2020-12-08 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_cpu_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
