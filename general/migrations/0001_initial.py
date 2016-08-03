# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_description', models.TextField()),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(default='India', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]