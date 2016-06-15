# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0115_registrationpage_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationpage',
            name='attachment',
            field=models.FileField(blank=True, help_text='A file field.  Feel free to add whatever you want to this email.', upload_to='uploads/internal', verbose_name='Maybe a PDF with some information?'),
        ),
    ]