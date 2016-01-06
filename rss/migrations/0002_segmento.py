# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rss.Grupo')),
            ],
        ),
    ]
