# Generated by Django 4.2.5 on 2023-12-09 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('work_hours', models.JSONField()),
                ('master_status', models.CharField(choices=[('active', 'ACTIVE'), ('passive', 'PASSIVE')])),
                ('gender', models.CharField(choices=[('erkak', 'Erkak'), ('ayol', 'Ayol')])),
                ('languages', models.CharField(max_length=250)),
                ('experiance', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_master', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Master',
                'verbose_name_plural': 'Masters',
            },
        ),
    ]
