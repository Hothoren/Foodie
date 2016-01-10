# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('food_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ident',
            fields=[
                ('ident_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ident_Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food_id', models.ForeignKey(to='takeout.Food')),
                ('ident_id', models.ForeignKey(to='takeout.Ident')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('shop_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('user_password', models.CharField(max_length=16)),
                ('user_school', models.CharField(max_length=20)),
            ],
        ),
    ]
