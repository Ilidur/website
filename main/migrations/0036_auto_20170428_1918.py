# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-28 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20170428_1918'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='gocardlessmandate',
            table='gocardlessmandate',
        ),
        migrations.AlterModelTable(
            name='gocardlesspayment',
            table='gocardlesspayment',
        ),
        migrations.AlterModelTable(
            name='space',
            table='space',
        ),
        migrations.AlterModelTable(
            name='supportermembership',
            table='supportermembership',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
    ]
