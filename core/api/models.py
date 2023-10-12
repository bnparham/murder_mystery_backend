from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    passport_number = models.IntegerField()
    license_plate = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'


class PhoneCalls(models.Model):
    caller = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='outgoing_calls')
    reciver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='incoming_calls')
    date = models.DateField()
    duration = models.IntegerField()

    class Meta:
        verbose_name = 'phone call'
        verbose_name_plural = 'phone calls'


class Location(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = "Locations"


class Street(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'


class BankAccount(models.Model):
    account_number = models.IntegerField()
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    created = models.DateField()

    class Meta:
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Accounts'


class AtmTransaction(models.Model):
    account_number = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    atm_location = models.ForeignKey(Street, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Atm Transaction'
        verbose_name_plural = 'Atm Transactions'


class SecurityLog(models.Model):
    license_plate = models.ForeignKey(Person, on_delete=models.CASCADE)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'Security Log'
        verbose_name_plural = 'Security Logs'


class CrimeSceneReport(models.Model):
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date = models.DateField()

    class Meta:
        verbose_name = 'Crime Scene Report'
        verbose_name_plural = 'Crime Scene Reports'


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Evidence(models.Model):
    crime_id = models.ForeignKey(CrimeSceneReport, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Evidence'
        verbose_name_plural = 'Evidences'


class Airports(models.Model):
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'


class Flights(models.Model):
    origin_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='departing_flights')
    destination_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='arriving_flights')
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'


class Passengers(models.Model):
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    seat = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'


class Interviews(models.Model):
    name = models.CharField(max_length=200)
    transcript = models.CharField(max_length=500)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        verbose_name = 'Interview'
        verbose_name_plural = 'Interviews'


class MessageBox(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    date = models.DateField()

    class Meta:
        verbose_name = 'Message Box'
        verbose_name_plural = 'Message Boxes'


class player_reply(models.Model):
    message_id = models.ForeignKey(MessageBox, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Player Reply'
        verbose_name_plural = 'Player Replies'


class npc_reply(models.Model):
    player_reply_id = models.ForeignKey(player_reply, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Npc Reply'
        verbose_name_plural = 'npc Replies'
