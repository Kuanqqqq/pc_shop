# Generated by Django 3.1.3 on 2020-12-09 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('service', '0016_auto_20201209_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.customer'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='date_ordered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
