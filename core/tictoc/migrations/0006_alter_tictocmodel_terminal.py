# Generated by Django 4.2.6 on 2023-12-03 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictoc', '0005_alter_tictocmodel_action_alter_tictocmodel_board_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictocmodel',
            name='terminal',
            field=models.BooleanField(blank=True, max_length=100, null=True),
        ),
    ]
