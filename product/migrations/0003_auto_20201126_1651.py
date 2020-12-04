# Generated by Django 3.1.3 on 2020-11-26 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201126_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpu',
            name='socket',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='motherboard',
            name='socket',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='build',
            name='gpu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.gpu'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='voltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cpu_cooler',
            name='voltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='voltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='voltage',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='power_supply',
            name='voltage',
            field=models.FloatField(),
        ),
    ]