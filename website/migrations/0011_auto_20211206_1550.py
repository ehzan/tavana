# Generated by Django 3.2.8 on 2021-12-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_rename_current_semester_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['semester', 'order']},
        ),
        migrations.AddField(
            model_name='course',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]