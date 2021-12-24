# Generated by Django 3.2.8 on 2021-12-18 21:18

import datetime
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_auto_20211210_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='highlight',
            name='visible',
        ),
        migrations.AddField(
            model_name='highlight',
            name='body',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='highlight',
            name='header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='highlight',
            name='icon',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2021, 12, 19), null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='date',
            field=django_jalali.db.models.jDateField(default=datetime.date(2021, 12, 19), null=True),
        ),
    ]