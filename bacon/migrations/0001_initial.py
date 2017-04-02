# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 14:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='DesignFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_free', models.BooleanField()),
                ('thickness', models.DecimalField(decimal_places=4, max_digits=10)),
                ('design', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='bacon.Design')),
            ],
        ),
    ]
