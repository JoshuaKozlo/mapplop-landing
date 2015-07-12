# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_signup_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='user_type',
            field=models.CharField(verbose_name='Type', max_length=255, null=True, blank=True),
        ),
    ]
