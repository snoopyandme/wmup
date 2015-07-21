# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logincnter', '0002_auto_20150721_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
