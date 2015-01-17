# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('nick_name', models.CharField(max_length=100)),
                ('personal_id', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('telephon_number', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
                ('work_place', models.CharField(max_length=100, null=True, blank=True)),
                ('move_in_date', models.DateField()),
                ('move_out_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
