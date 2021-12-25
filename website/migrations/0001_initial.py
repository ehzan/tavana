# Generated by Django 3.2.8 on 2021-12-25 11:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=50, unique=True)),
                ('persian_name', models.CharField(max_length=50, unique=True)),
                ('order', models.IntegerField(default=10)),
                ('category', models.CharField(max_length=50)),
                ('cv', models.TextField()),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('whatsappId', models.CharField(blank=True, max_length=50, null=True)),
                ('instagramId', models.CharField(blank=True, max_length=50, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(blank=True, max_length=1000, null=True)),
                ('icon', models.CharField(blank=True, max_length=1000, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('order', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_filename', models.CharField(blank=True, max_length=50, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('link_caption', models.CharField(default='more‥', max_length=1000)),
                ('header', models.BooleanField(default=False)),
                ('body', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=10)),
                ('date', django_jalali.db.models.jDateField(default=datetime.date(2021, 12, 25), null=True)),
                ('image_filename_1', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_filename_2', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_filename_3', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption_3', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['order', 'date'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image_filename_1', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_filename_2', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_filename_3', models.CharField(blank=True, max_length=50, null=True)),
                ('image_caption_3', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('embed_code', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=10)),
            ],
            options={
                'ordering': ['order', '-order'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=10)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.semester')),
            ],
            options={
                'ordering': ['semester', 'order'],
            },
        ),
    ]
