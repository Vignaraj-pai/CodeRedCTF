# Generated by Django 4.2.10 on 2024-08-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf_backend', '0005_question_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='team',
            name='highest_section_reached',
            field=models.IntegerField(default=1),
        ),
    ]
