# Generated by Django 3.2.8 on 2021-12-05 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_highlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highlight',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='highlight',
            name='image_filename',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
