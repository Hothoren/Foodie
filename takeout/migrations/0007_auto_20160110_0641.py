# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeout', '0006_auto_20160110_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMan',
            fields=[
                ('deliveryman_id', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('deliveryman_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='food_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='shop_id',
            field=models.ForeignKey(to='takeout.Shop', null=True),
        ),
        migrations.AddField(
            model_name='ident',
            name='deliveryman_id',
            field=models.ForeignKey(to='takeout.DeliveryMan', null=True),
        ),
    ]
