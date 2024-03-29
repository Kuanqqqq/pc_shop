# Generated by Django 3.1.3 on 2020-11-26 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.CharField(max_length=200)),
                ('voltage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cpu_cooler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooler', models.CharField(max_length=200)),
                ('voltage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpu', models.CharField(max_length=200)),
                ('voltage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motherboard', models.CharField(max_length=200)),
                ('voltage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Power_supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(max_length=200)),
                ('voltage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooler', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.cpu_cooler')),
                ('cpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.cpu')),
                ('gpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.gpu')),
                ('memory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.memory')),
                ('motherboard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.motherboard')),
                ('power', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.power_supply')),
            ],
        ),
    ]
