# Generated by Django 2.0.5 on 2018-07-28 00:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 28, 0, 23, 48, 980601, tzinfo=utc))),
            ],
        ),
    ]
