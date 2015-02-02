# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions_and_ratings', '0002_auto_20150202_0640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(default=datetime.datetime(2015, 2, 2, 12, 40, 44, 561510, tzinfo=utc))),
                ('end', models.DateTimeField()),
                ('show_results_before_end', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=200)),
                ('multiple_answers', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(to='questions_and_ratings.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('question', models.ForeignKey(to='questions_and_ratings.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='QuestionVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 2, 2, 12, 40, 44, 562830, tzinfo=utc))),
                ('answers', models.ManyToManyField(to='questions_and_ratings.QuestionAnswer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(default=datetime.datetime(2015, 2, 2, 12, 40, 44, 561510, tzinfo=utc))),
                ('end', models.DateTimeField()),
                ('show_results_before_end', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=200)),
                ('max', models.IntegerField()),
                ('type', models.CharField(max_length=10, choices=[(b'STARS', b'stars rating'), (b'SLIDER', b'slider rating'), (b'LIKES', b'like rating')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RatingPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('rating', models.ForeignKey(to='questions_and_ratings.Rating')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='RatingVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 2, 2, 12, 40, 44, 562830, tzinfo=utc))),
                ('value', models.IntegerField()),
                ('rating', models.ForeignKey(to='questions_and_ratings.Rating')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
