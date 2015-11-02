# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='matriaspirant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('profilepic', models.ImageField(null=True, upload_to='images/%Y/%m/%d', verbose_name='Profile Pic')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')),
                ('dob', models.DateField()),
                ('tob', models.CharField(max_length=12)),
                ('height', models.DecimalField(max_digits=2, decimal_places=1)),
                ('complexion', models.CharField(max_length=1, choices=[('L', 'Light'), ('F', 'Fair'), ('W', 'Wheatish'), ('D', 'Dark')], default='L')),
                ('caste', models.CharField(max_length=30)),
                ('birth_place', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=100)),
                ('course_hobbie', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=30)),
                ('business', models.CharField(max_length=30)),
                ('agriculture', models.CharField(max_length=30)),
                ('house', models.CharField(max_length=50)),
                ('income', models.CharField(max_length=10)),
                ('father_occupation', models.CharField(max_length=30)),
                ('mother_occupation', models.CharField(max_length=30)),
                ('father_name', models.CharField(max_length=50)),
                ('father_nativeplace', models.CharField(max_length=50)),
                ('mother_nativeplace', models.CharField(max_length=50)),
                ('num_brothers', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('num_brothers_married', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('num_brothers_unmarried', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('num_sisters', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('num_sisters_married', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('num_sisters_unmarried', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('expectations', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=12)),
                ('mobile', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
