# Generated by Django 5.2.3 on 2025-07-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findjobapp', '0007_applicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='status',
            field=models.TextField(default='pending', null=True),
        ),
    ]
