# Generated by Django 4.0.4 on 2022-04-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_oilchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='oilchange',
            name='miles',
            field=models.IntegerField(default=0),
        ),
    ]
