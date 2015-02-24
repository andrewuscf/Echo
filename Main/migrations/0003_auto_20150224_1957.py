# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_userplaylisttrack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplaylisttrack',
            name='order',
            field=models.SmallIntegerField(default=1, unique=True),
            preserve_default=True,
        ),
    ]
