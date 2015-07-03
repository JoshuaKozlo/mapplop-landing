# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='id',
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
    ]
