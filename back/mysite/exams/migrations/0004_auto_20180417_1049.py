# Generated by Django 2.0.4 on 2018-04-17 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20180417_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='corrent_number',
            new_name='correct_number',
        ),
    ]
