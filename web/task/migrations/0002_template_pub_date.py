# Generated by Django 3.2.4 on 2021-06-20 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 20, 15, 35, 6, 851553), verbose_name='date retrieved'),
        ),
    ]
