# Generated by Django 4.1.5 on 2023-01-31 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_merge_20230131_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='current_week_recipes',
        ),
    ]
