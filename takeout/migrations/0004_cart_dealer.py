# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('takeout', '0003_auto_20160110_0318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_id', models.ForeignKey(to='takeout.Food')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('dealer_id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('dealer_name', models.CharField(max_length=20)),
            ],
        ),
    ]
