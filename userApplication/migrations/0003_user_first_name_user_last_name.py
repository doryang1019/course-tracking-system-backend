# Generated by Django 4.1.13 on 2024-07-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApplication', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]