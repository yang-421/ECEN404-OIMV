# Generated by Django 2.0.4 on 2018-04-18 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20180417_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='mouse_moves',
        ),
    ]
