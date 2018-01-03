# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname1', models.CharField(max_length=100, null=True, blank=True)),
                ('phone1', models.CharField(max_length=100)),
                ('email1', models.EmailField(max_length=100)),
                ('pname2', models.CharField(max_length=100)),
                ('phone2', models.CharField(max_length=100)),
                ('email2', models.EmailField(max_length=100)),
                ('level', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('fibonacci_status', models.IntegerField(default=0)),
                ('fib_plus', models.IntegerField(default=5)),
                ('fib_minus', models.IntegerField(default=3)),
                ('fibonacci_marks', models.IntegerField(default=0)),
                ('f_counter', models.IntegerField(default=3)),
                ('coins_status', models.IntegerField(default=0)),
                ('skips', models.IntegerField(default=0)),
                ('coins', models.IntegerField(default=3)),
                ('start_time', models.IntegerField(default=0)),
                ('end_time', models.IntegerField(default=0)),
                ('right_count', models.IntegerField(default=0)),
                ('wrong_count', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qattempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=1000000)),
                ('option_a', models.CharField(max_length=500)),
                ('option_b', models.CharField(max_length=500)),
                ('option_c', models.CharField(max_length=500)),
                ('option_d', models.CharField(max_length=500)),
                ('correct_option', models.CharField(max_length=1)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='qattempt',
            name='question',
            field=models.ForeignKey(to='clash.Question'),
        ),
        migrations.AddField(
            model_name='qattempt',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
