# Generated by Django 2.2.13 on 2020-09-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0005_auto_20200905_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='creationdate',
            field=models.DateTimeField(verbose_name='Creation Date'),
        ),
    ]
