# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, default=b'Tell everyone something about yourself', verbose_name='about')),
                ('gender', models.CharField(choices=[(b'M', 'Male'), (b'F', 'Female')], default=b'None', help_text=b'What are ya?', max_length=5, null=True, verbose_name='gender')),
                ('url', models.URLField(blank=True, verbose_name='url')),
                ('location', models.CharField(blank=True, default=b'', max_length=150, verbose_name='location')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
    ]
