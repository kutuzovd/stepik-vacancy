# Generated by Django 3.0.5 on 2020-04-07 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('junvac', '0005_auto_20200407_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='vacancies',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacancy', to='junvac.Vacancy'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='junvac.Company'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='speciality',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='speciality', to='junvac.Speciality'),
        ),
    ]