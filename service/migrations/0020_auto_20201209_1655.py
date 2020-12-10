# Generated by Django 3.1.3 on 2020-12-09 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('service', '0019_remove_orderitems_order_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
