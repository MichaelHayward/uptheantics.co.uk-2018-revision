# Generated by Django 2.0.6 on 2018-06-26 10:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20180626_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='gig_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 6, 26, 10, 55, 14, 442293, tzinfo=utc)),
        ),
    ]
