# Generated by Django 2.0.8 on 2018-11-09 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0011_auto_20181108_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlfilter',
            name='slug',
            field=models.SlugField(default='placeholder'),
            preserve_default=False,
        ),
    ]
