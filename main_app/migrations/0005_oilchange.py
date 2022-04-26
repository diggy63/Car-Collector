# Generated by Django 4.0.4 on 2022-04-26 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_car_miles'),
    ]

    operations = [
        migrations.CreateModel(
            name='OilChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('oiltype', models.CharField(choices=[('FS', 'Full Synthectic'), ('S', 'Syntethic'), ('C', 'Conventional'), ('HM', 'High Mileage')], default='FS', max_length=2)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.car')),
            ],
        ),
    ]
