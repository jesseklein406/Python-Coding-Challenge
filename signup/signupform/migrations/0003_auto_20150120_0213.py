# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signupform', '0002_auto_20150118_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name_input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='email_input',
            name='person',
            field=models.ForeignKey(to='signupform.Name_input', null=True),
            preserve_default=True,
        ),
    ]
