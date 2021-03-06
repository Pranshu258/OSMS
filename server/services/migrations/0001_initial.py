# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-15 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Batch')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installments', models.IntegerField()),
                ('amountPerInst', models.IntegerField()),
                ('paidInst', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('father', models.CharField(max_length=255)),
                ('mother', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'O', b'Other')], max_length=6)),
                ('address', models.CharField(max_length=2048)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Batch')),
            ],
        ),
        migrations.AddField(
            model_name='grades',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Student'),
        ),
        migrations.AddField(
            model_name='fee',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Student'),
        ),
    ]
