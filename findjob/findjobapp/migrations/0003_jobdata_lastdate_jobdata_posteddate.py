# Generated by Django 5.2.3 on 2025-07-01 13:27

import datetime
import findjobapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findjobapp', '0002_jobdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdata',
            name='lastdate',
            field=models.DateField(default=findjobapp.models.get_due_date),
        ),
        migrations.AddField(
            model_name='jobdata',
            name='posteddate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
