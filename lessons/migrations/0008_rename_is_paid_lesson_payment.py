# Generated by Django 5.0.3 on 2024-11-10 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_rename_payment_lesson_is_paid_alter_lesson_cash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='is_paid',
            new_name='payment',
        ),
    ]
