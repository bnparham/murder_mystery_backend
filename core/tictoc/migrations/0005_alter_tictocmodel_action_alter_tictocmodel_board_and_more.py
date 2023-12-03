# Generated by Django 4.2.6 on 2023-12-03 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictoc', '0004_alter_tictocmodel_board_alter_tictocmodel_player_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tictocmodel',
            name='action',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tictocmodel',
            name='board',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tictocmodel',
            name='move',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tictocmodel',
            name='player',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tictocmodel',
            name='terminal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tictocmodel',
            name='winner',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]