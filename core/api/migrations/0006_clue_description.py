# Generated by Django 4.2.6 on 2023-10-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_description_clue_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='clue',
            name='description',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]
