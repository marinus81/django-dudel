# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PossibleDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possible_dates', to='datefinder.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='maybe',
            field=models.ManyToManyField(related_name='maybe_answers', to='datefinder.PossibleDate'),
        ),
        migrations.AddField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='datefinder.Poll'),
        ),
        migrations.AddField(
            model_name='answer',
            name='yes',
            field=models.ManyToManyField(related_name='positive_answers', to='datefinder.PossibleDate'),
        ),
    ]
