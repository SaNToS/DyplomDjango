# Generated by Django 3.1.3 on 2023-05-07 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_lesson_number_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='number_lesson',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='schedule.call'),
        ),
    ]
