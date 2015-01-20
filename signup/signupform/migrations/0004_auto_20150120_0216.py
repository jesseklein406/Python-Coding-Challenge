# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupform', '0003_auto_20150120_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_input',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]
