# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeout', '0002_foodieuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodieuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='foodieuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='FoodieUser',
        ),
    ]
