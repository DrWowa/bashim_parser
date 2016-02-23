# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BashImData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.PositiveIntegerField(verbose_name='Номер цитаты')),
                ('text', models.TextField(verbose_name='Текст цитаты')),
            ],
            options={
                'verbose_name': 'Цитата bash.im',
                'verbose_name_plural': 'Цитаты bash.im',
            },
        ),
    ]
