# Generated by Django 2.0.6 on 2018-07-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('blog', '0038_auto_20180703_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogtagindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='intro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='location_link',
            field=models.CharField(default='https://www.uptheantics.co.uk', max_length=2083),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='ticket_link',
            field=models.CharField(default='https://www.uptheantics.co.uk', max_length=2083),
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.DeleteModel(
            name='BlogTagIndexPage',
        ),
    ]
    atomic=False
