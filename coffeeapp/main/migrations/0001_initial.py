# Generated by Django 4.0.6 on 2022-07-14 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=1024)),
                ('coordinates', models.JSONField()),
                ('opening_hours', models.CharField(max_length=128)),
            ],
        ),
    ]