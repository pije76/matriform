# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='matriaspirant',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('profilepic', models.ImageField(upload_to='images/%Y/%m/%d', blank=True, null=True, verbose_name='Profile Pic')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, default='M')),
                ('matriaspirant_status', models.CharField(choices=[('F', 'Fresh'), ('M', 'Married'), ('B', 'Bin')], max_length=1, default='F')),
                ('dob', models.DateField()),
                ('tob', models.CharField(max_length=12, blank=True, null=True)),
                ('height', models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)),
                ('complexion', models.CharField(choices=[('L', 'Light'), ('F', 'Fair'), ('W', 'Wheatish'), ('D', 'Dark')], blank=True, null=True, default='L', max_length=1)),
                ('blood_group', models.CharField(choices=[('O+', 'O +'), ('O-', 'O -'), ('A+', 'A +'), ('A-', 'A -'), ('B+', 'B +'), ('B-', 'B -'), ('AB+', 'AB +'), ('AB-', 'AB -')], blank=True, null=True, default='L', max_length=1)),
                ('caste', models.CharField(max_length=30)),
                ('birth_place', models.CharField(max_length=30, blank=True, null=True)),
                ('qualification', models.CharField(max_length=100)),
                ('course_hobbie', models.CharField(max_length=100, blank=True, null=True)),
                ('occupation', models.CharField(max_length=30, blank=True, null=True)),
                ('business', models.CharField(max_length=30, blank=True, null=True)),
                ('agriculture', models.CharField(max_length=30, blank=True, null=True)),
                ('house', models.CharField(max_length=50, blank=True, null=True)),
                ('income', models.CharField(max_length=10, blank=True, null=True)),
                ('father_occupation', models.CharField(max_length=30, blank=True, null=True)),
                ('mother_occupation', models.CharField(max_length=30, blank=True, null=True)),
                ('father_name', models.CharField(max_length=50, blank=True, null=True)),
                ('father_nativeplace', models.CharField(max_length=50, blank=True, null=True)),
                ('father_nativeplace_district', models.CharField(max_length=50)),
                ('mother_nativeplace', models.CharField(max_length=50, blank=True, null=True)),
                ('num_brothers', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True)),
                ('num_brothers_married', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True)),
                ('num_brothers_unmarried', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True)),
                ('num_sisters', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True)),
                ('num_sisters_married', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True)),
                ('num_sisters_unmarried', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True)),
                ('expectations', models.CharField(max_length=200, blank=True, null=True)),
                ('address', models.CharField(max_length=400, blank=True, null=True)),
                ('address_district', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=12, blank=True, null=True)),
                ('mobile', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
