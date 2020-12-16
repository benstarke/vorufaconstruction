# Generated by Django 3.1.4 on 2020-12-15 21:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='homepage')),
            ],
            options={
                'verbose_name_plural': 'index',
            },
        ),
        migrations.CreateModel(
            name='myprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='profile')),
            ],
            options={
                'verbose_name_plural': 'myprofile',
            },
        ),
        migrations.CreateModel(
            name='myservices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Fittings', 'Fittings'), ('Wiring', 'Wiring'), ('Tiles', 'Tiles'), ('Ceilings', 'Ceilings'), ('Plumbing', 'Plumbing'), ('Painting', 'Painting')], max_length=15)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='services')),
                ('last_update', models.DateTimeField(verbose_name=datetime.datetime(2020, 12, 15, 21, 20, 25, 74280, tzinfo=utc))),
            ],
            options={
                'verbose_name_plural': 'myservices',
                'ordering': ['-last_update'],
            },
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='homepage')),
            ],
            options={
                'verbose_name_plural': 'slider',
            },
        ),
        migrations.CreateModel(
            name='workexperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='myworkexperience')),
            ],
            options={
                'verbose_name_plural': 'workexperience',
            },
        ),
    ]