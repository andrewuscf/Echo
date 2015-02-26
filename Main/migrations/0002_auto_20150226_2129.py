# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(default=b'example.jpg', upload_to=b'')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPlaylistTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playlist', models.ForeignKey(to='Main.Playlist')),
                ('track', models.OneToOneField(to='Main.Track')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_online', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='usermusic',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserMusic',
        ),
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(blank=True, to='Main.Album', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='previewURL',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
