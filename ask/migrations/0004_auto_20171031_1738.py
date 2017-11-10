# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='dislikes',
            field=models.IntegerField(),
        ),
    ]
