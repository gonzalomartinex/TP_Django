# Generated by Django 4.2.4 on 2023-12-07 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Streaming', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
    ]