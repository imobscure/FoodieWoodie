# Generated by Django 4.2.1 on 2023-06-23 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='food',
        ),
    ]