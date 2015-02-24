# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlaylistTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.SmallIntegerField(default=1)),
                ('playlist', models.OneToOneField(to='Main.Playlist')),
                ('track', models.ForeignKey(to='Main.Track')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
