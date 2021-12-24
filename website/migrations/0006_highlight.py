# Generated by Django 3.2.8 on 2021-12-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_coach_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('image_filename', models.CharField(max_length=50)),
                ('order', models.IntegerField(default=1)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]