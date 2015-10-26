# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriaspirants',
            name='profilepic',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
