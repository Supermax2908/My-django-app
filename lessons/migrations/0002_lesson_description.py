# Generated by Django 5.1.2 on 2024-10-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
