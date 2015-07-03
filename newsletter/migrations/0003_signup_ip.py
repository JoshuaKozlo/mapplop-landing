# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150703_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='ip',
            field=models.GenericIPAddressField(default=''),
            preserve_default=False,
        ),
    ]
