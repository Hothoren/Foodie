# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeout', '0005_auto_20160110_0551'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ident_food',
            unique_together=set([('ident_id', 'food_id')]),
        ),
    ]
