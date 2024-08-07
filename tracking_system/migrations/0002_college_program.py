# Generated by Django 4.1.13 on 2024-07-03 23:41

from django.db import migrations, models
import djongo.models.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tracking_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('term', models.IntegerField(default=3)),
                ('courses', djongo.models.fields.JSONField(default=list)),
                ('collegeId', models.UUIDField()),
            ],
        ),
    ]
