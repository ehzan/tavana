# Generated by Django 3.2.8 on 2021-12-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_rename_jalalidate_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]