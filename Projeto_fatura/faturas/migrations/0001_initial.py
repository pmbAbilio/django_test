# Generated by Django 2.1.7 on 2019-03-29 00:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fatura',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vendedor', models.TextField()),
                ('data', models.DateField(default=datetime.datetime(2019, 3, 29, 0, 3, 7, 509114, tzinfo=utc))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
