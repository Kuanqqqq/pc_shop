# Generated by Django 3.1.3 on 2020-12-02 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_memory_voltage'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='user_token',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]