# Generated by Django 3.2.8 on 2021-12-08 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20211208_0410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='image_caption_4',
        ),
        migrations.RemoveField(
            model_name='page',
            name='image_filename_4',
        ),
    ]
