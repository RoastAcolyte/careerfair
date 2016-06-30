# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0122_auto_20160618_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='friday_representatives',
            field=models.ManyToManyField(blank=True, related_name='fri_reps', to='theme.CompanyRep'),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='saturday_representatives',
            field=models.ManyToManyField(blank=True, related_name='sat_reps', to='theme.CompanyRep'),
        ),
    ]