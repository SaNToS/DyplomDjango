# Generated by Django 3.1.3 on 2023-05-07 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_lesson_schedule_weekday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='days',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='name_lesson',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='number_lesson',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]