# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 19:17
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
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='dataset')),
                ('name', models.CharField(max_length=50)),
                ('scope', models.CharField(max_length=50)),
                ('parse_result', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('column_data', models.TextField()),
                ('rowcount', models.IntegerField()),
                ('colcount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=50)),
                ('alrorithm', models.CharField(max_length=255)),
                ('algorithm_param', models.CharField(max_length=255)),
                ('column', models.CharField(max_length=255)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinator.DataSet')),
            ],
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('validation', models.CharField(max_length=20)),
                ('validation_param', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('autogroup', models.BooleanField(default=False)),
                ('algorithms', models.TextField()),
                ('metric', models.CharField(max_length=50)),
                ('timelimit', models.IntegerField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinator.DataSet')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('visibility', models.CharField(max_length=10)),
                ('task', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinator.Project'),
        ),
        migrations.AddField(
            model_name='emodel',
            name='experiment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coordinator.Experiment'),
        ),
        migrations.AddField(
            model_name='dataset',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coordinator.Project'),
        ),
    ]
