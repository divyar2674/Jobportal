# Generated by Django 5.2.3 on 2025-07-02 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findjobapp', '0004_jobseekerdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseekerregistraion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=15)),
                ('qualification', models.TextField()),
                ('skills', models.TextField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='findjobapp.jobdata')),
            ],
        ),
        migrations.DeleteModel(
            name='Jobseekerdata',
        ),
    ]
