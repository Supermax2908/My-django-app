# Generated by Django 5.0.3 on 2024-11-10 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_alter_lessontag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='payment',
            new_name='is_paid',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='cash',
            field=models.IntegerField(),
        ),
    ]
