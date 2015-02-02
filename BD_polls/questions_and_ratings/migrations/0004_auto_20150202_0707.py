# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions_and_ratings', '0003_question_questionanswer_questionplugin_questionvote_rating_ratingplugin_ratingvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 13, 7, 29, 575227, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='questionvote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 13, 7, 29, 576457, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rating',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 13, 7, 29, 575227, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ratingvote',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 2, 13, 7, 29, 576457, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
