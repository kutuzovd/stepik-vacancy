# Generated by Django 3.0.5 on 2020-04-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('junvac', '0006_auto_20200407_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
