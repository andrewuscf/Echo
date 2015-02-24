# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20150224_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userplaylisttrack',
            name='order',
            field=models.SmallIntegerField(default=1),
            preserve_default=True,
        ),
    ]
