# Generated by Django 2.0.4 on 2018-04-17 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20180417_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user_id',
            new_name='student_id',
        ),
    ]
