# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shifts_app', '0002_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='current_user',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
