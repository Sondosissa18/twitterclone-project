# Generated by Django 3.1.3 on 2020-12-01 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20201130_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='title',
        ),
    ]
