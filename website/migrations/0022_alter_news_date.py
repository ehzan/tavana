# Generated by Django 3.2.8 on 2021-12-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_alter_news_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
