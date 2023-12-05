# Generated by Django 4.2.4 on 2023-11-25 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Streaming', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contraseña',
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=True, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=False),
        ),
    ]
