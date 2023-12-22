# Generated by Django 4.2.5 on 2023-12-22 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services_order', to='services.services'),
        ),
    ]
