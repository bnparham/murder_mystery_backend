# Generated by Django 4.2.6 on 2023-10-11 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CrimeSceneReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('type', models.CharField(max_length=200)),
                ('destination_airport_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arriving_flights', to='api.airports')),
                ('origin_airport_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departing_flights', to='api.airports')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MessageBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('passport_number', models.IntegerField()),
                ('license_plate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('license_plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
                ('street_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.street')),
            ],
        ),
        migrations.CreateModel(
            name='player_reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.messagebox')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCalls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.IntegerField()),
                ('caller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_calls', to='api.person')),
                ('reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_calls', to='api.person')),
            ],
        ),
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=200)),
                ('flight_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.flights')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
        ),
        migrations.CreateModel(
            name='npc_reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=500)),
                ('player_reply_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player_reply')),
            ],
        ),
        migrations.AddField(
            model_name='messagebox',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person'),
        ),
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('transcript', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crime_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.crimescenereport')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.item')),
            ],
        ),
        migrations.AddField(
            model_name='crimescenereport',
            name='street_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.street'),
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('created', models.DateField()),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.person')),
            ],
        ),
        migrations.CreateModel(
            name='AtmTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('account_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bankaccount')),
                ('atm_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.street')),
            ],
        ),
    ]
