# Generated by Django 5.1.2 on 2024-10-31 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions_answers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='lesson',
        ),
    ]
