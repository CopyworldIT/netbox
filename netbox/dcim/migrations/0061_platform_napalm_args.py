# Generated by Django 2.0.6 on 2018-06-29 15:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0060_change_logging'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform',
            name='napalm_args',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='Additional arguments to pass when initiating the NAPALM driver (JSON format)', null=True, verbose_name='NAPALM arguments'),
        ),
    ]
