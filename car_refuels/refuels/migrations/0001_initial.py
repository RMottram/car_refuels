# Generated by Django 4.2.11 on 2024-03-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefuelSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fuel_type', models.CharField(max_length=20)),
                ('pence_per_litre', models.DecimalField(decimal_places=1, max_digits=4)),
                ('litres_filled', models.DecimalField(decimal_places=2, max_digits=4)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
