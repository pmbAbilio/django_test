# Generated by Django 2.1.7 on 2019-03-30 00:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('faturas', '0008_auto_20190329_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fatura',
            name='Client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fatura',
            name='Data',
            field=models.DateField(default=datetime.datetime(2019, 3, 30, 0, 45, 21, 779028, tzinfo=utc)),
        ),
    ]