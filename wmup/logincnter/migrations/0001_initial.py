# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_model',
            fields=[
                ('username', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
