# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20150703_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='user_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
