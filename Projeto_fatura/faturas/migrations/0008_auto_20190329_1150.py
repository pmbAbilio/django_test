# Generated by Django 2.1.7 on 2019-03-29 11:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('faturas', '0007_auto_20190329_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatura',
            name='Data',
            field=models.DateField(default=datetime.datetime(2019, 3, 29, 11, 50, 48, 247895, tzinfo=utc)),
        ),
    ]
