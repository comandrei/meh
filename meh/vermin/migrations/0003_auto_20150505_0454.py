# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vermin', '0002_auto_20150505_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eh',
            name='post',
            field=models.ForeignKey(to='vermin.Post'),
        ),
        migrations.AlterField(
            model_name='meh',
            name='post',
            field=models.ForeignKey(to='vermin.Post'),
        ),
    ]
