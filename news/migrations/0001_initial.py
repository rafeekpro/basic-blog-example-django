# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nazwa Kategorii')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Odnosnik')),
                ('icon', models.ImageField(blank=True, upload_to='icons', verbose_name='Ikonka Kategorii')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tytul')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Odnosnik')),
                ('text', models.TextField(verbose_name='Tresc')),
                ('posted_date', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('categories', models.ManyToManyField(to='news.Category', verbose_name='Kategorie')),
            ],
            options={
                'verbose_name': 'Wiadomosc',
                'verbose_name_plural': 'Wiadomosci',
            },
        ),
    ]
