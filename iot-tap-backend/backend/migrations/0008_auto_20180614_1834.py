# Generated by Django 2.0.2 on 2018-06-14 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_eerule_esrule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='capabilities',
            new_name='caps',
        ),
    ]
