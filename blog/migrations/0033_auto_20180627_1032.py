# Generated by Django 2.0.6 on 2018-06-27 09:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20180627_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='gig_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
    atomic=False
