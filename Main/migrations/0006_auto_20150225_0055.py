# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_userpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpicture',
            name='imageurl',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
