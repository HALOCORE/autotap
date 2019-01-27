# Generated by Django 2.0.2 on 2018-06-29 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20180621_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('is_current', models.BooleanField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.State')),
            ],
        ),
    ]