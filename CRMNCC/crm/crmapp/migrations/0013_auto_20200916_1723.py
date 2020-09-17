# Generated by Django 2.2.13 on 2020-09-16 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0012_auto_20200916_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestion',
            name='status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('closed', 'Closed')], default='open', max_length=1000, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='creationdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 16, 14, 23, 59, 412657, tzinfo=utc), verbose_name='Creation Date'),
        ),
    ]
