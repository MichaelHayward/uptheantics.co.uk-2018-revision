# Generated by Django 2.0.6 on 2018-06-24 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_bio_headshot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bio',
            options={'verbose_name_plural': 'bios'},
        ),
    ]
