# Generated by Django 2.1.3 on 2018-11-19 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=64)),
                ('passport_data', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_country', models.CharField(max_length=64)),
                ('departure_country', models.CharField(max_length=64)),
                ('destination_city', models.CharField(max_length=64)),
                ('departure_city', models.CharField(max_length=64)),
                ('destination_street', models.CharField(max_length=64)),
                ('departure_street', models.CharField(max_length=64)),
                ('destination_house', models.CharField(max_length=64)),
                ('departure_house', models.CharField(max_length=64)),
                ('destination_details', models.CharField(max_length=64)),
                ('departure_details', models.CharField(max_length=64)),
                ('cost', models.CharField(max_length=32)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_auto', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('capacity_weight', models.IntegerField(default=0)),
                ('capacity_volume', models.IntegerField(default=0)),
                ('driver', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trucking.Driver')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trucking.Order')),
            ],
        ),
    ]
