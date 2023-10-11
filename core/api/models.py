from django.db import models

class Person(models.Model):
    name = models.CharField()
    phone_number = models.IntegerField()
    passport_number = models.IntegerField()
    license_plate = models.CharField()

class PhoneCalls(models.Model):
    caller = models.ForeignKey(Person, on_delete=models.CASCADE)
    reciver = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()

class Location(models.Model):
    name = models.CharField()

class Street(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField()

class BankAccount(models.Model):
    account_number = models.IntegerField()
    person_id = models.ForeignKey(Person)
    created = models.DateField()

class AtmTransaction(models.Model):
    account_number = models.ForeignKey(BankAccount)
    atm_location = models.ForeignKey(Street, on_delete=models.CASCADE)
    transaction_type = models.CharField()
    amount = models.IntegerField()
    date = models.DateField()

class SecurityLog(models.Model):
    license_plate = models.ForeignKey(Person, on_delete=models.CASCADE)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    activity = models.CharField()
    date = models.DateField()
    time = models.TimeField()

class CrimeSceneReport(models.Model):
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
    description = models.CharField()
    date = models.DateField()

class Item(models.Model):
    name = models.CharField()
    description = models.CharField()

class Evidence(models.Model):
    crime_id = models.ForeignKey(CrimeSceneReport, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

class Airports(models.Model):
    full_name = models.CharField()
    city = models.CharField()

class Flights(models.Model):
    origin_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE)
    destination_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField()

class Passengers(models.Model):
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    seat = models.CharField()

class Interviews(models.Model):
    name = models.CharField()
    transcript = models.CharField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()

class MessageBox(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.CharField()
    date = models.DateField()

class player_reply(models.Model):
    message_id = models.ForeignKey(MessageBox, on_delete=models.CASCADE)
    body = models.CharField()

class npc_reply(models.Model):
    player_reply_id = models.ForeignKey(player_reply, on_delete=models.CASCADE)
    body = models.CharField()