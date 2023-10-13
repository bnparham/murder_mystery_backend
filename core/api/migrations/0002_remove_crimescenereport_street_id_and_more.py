# Generated by Django 4.2.6 on 2023-10-13 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crimescenereport',
            name='street_id',
        ),
        migrations.RemoveField(
            model_name='interviews',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='securitylog',
            name='location_id',
        ),
        migrations.AddField(
            model_name='crimescenereport',
            name='location_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.location'),
        ),
        migrations.AddField(
            model_name='interviews',
            name='street_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.street'),
        ),
    ]