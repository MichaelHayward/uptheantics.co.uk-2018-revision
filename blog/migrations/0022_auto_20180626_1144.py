# Generated by Django 2.0.6 on 2018-06-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20180626_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='gig_date',
            field=models.DateField(default='1066-10-14'),
        ),
    ]
