# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 01:15
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0124_auto_20160619_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationpage',
            name='email_message',
            field=mezzanine.core.fields.RichTextField(blank=True, help_text='Emails sent based on the above options will contain each of the form fields entered. You can also enter a message here that will be included in the email.', verbose_name='Message'),
        ),
    ]