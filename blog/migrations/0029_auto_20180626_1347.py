# Generated by Django 2.0.6 on 2018-06-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20180626_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='gig_time',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
