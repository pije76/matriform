# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='matriaspirant',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('profilepic', models.ImageField(null=True, verbose_name='Profile Pic', upload_to='images/%Y/%m/%d')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(default='M', max_length=1, choices=[('M', 'Male'), ('F', 'Female')])),
                ('dob', models.DateField()),
                ('tob', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('caste', models.CharField(max_length=30)),
                ('birth_place', models.CharField(max_length=30)),
                ('height', models.DecimalField(decimal_places=2, max_digits=3)),
                ('complexion', models.CharField(default='L', max_length=1, choices=[('L', 'Light'), ('F', 'Fair'), ('W', 'Wheatish'), ('D', 'Dark')])),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
