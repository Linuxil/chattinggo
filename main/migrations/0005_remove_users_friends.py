# Generated by Django 5.0.1 on 2024-01-20 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_users_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='friends',
        ),
    ]