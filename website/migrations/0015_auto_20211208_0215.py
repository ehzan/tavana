# Generated by Django 3.2.8 on 2021-12-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20211208_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image_filename_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='image_filename_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='image_filename_5',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]