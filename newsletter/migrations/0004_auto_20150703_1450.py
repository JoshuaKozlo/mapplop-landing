# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_signup_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(primary_key=True, verbose_name='Email', serialize=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(verbose_name='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='signup',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='IP', default='0.0.0.0'),
        ),
    ]
