# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0003_auto_20170610_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=5000, null=True)),
                ('status', models.IntegerField(default=1)),
                ('create_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('modified_datetime', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'stories',
            },
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lover_id',
            new_name='lover',
        ),
        migrations.AddField(
            model_name='media',
            name='create_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='modified_datetime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='story',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Media'),
        ),
        migrations.AddField(
            model_name='story',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.User'),
        ),
    ]
