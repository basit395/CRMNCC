# Generated by Django 2.2.13 on 2020-09-06 21:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0006_auto_20200906_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 6, 21, 7, 56, 795669, tzinfo=utc), verbose_name='Creation Date'),
        ),
    ]
