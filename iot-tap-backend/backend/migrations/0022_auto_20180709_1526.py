# Generated by Django 2.0.2 on 2018-07-09 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_auto_20180709_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setcapopt',
            old_name='set',
            new_name='cap',
        ),
    ]
