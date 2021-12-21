# Generated by Django 3.0.5 on 2021-12-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('classification', models.CharField(max_length=30)),
                ('type', models.CharField(default='user', max_length=30)),
                ('title', models.TextField()),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('completion', models.CharField(default=False, max_length=30)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
