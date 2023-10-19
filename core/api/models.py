from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    passport_number = models.IntegerField()
    license_plate = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def __str__(self):
        return self.name


class PhoneCalls(models.Model):
    caller = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='outgoing_calls')
    reciver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='incoming_calls')
    date = models.DateField()
    duration = models.IntegerField()

    class Meta:
        verbose_name = 'phone call'
        verbose_name_plural = 'phone calls'

    def __str__(self):
        return f'{self.caller}-{self.reciver}'


class Location(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class Street(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Street'
        verbose_name_plural = 'Streets'

    def __str__(self):
        return f'{self.location_id} - {self.name}'


class BankAccount(models.Model):
    account_number = models.IntegerField()
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    created = models.DateField()

    class Meta:
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Accounts'

    def __str__(self):
        return f'{self.account_number} - {self.person_id}'


class AtmTransaction(models.Model):
    account_number = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    atm_location = models.ForeignKey(Street, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=200)
    amount = models.IntegerField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Atm Transaction'
        verbose_name_plural = 'Atm Transactions'

    def __str__(self):
        return f'{self.account_number} - {self.atm_location}'


class SecurityLog(models.Model):
    license_plate = models.ForeignKey(Person, on_delete=models.CASCADE)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE)
    activity = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'Security Log'
        verbose_name_plural = 'Security Logs'

    def __str__(self):
        return f'{self.license_plate} - {self.street_id}'


class CrimeSceneReport(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, default=None)
    description = models.CharField(max_length=200)
    date = models.DateField()

    class Meta:
        verbose_name = 'Crime Scene Report'
        verbose_name_plural = 'Crime Scene Reports'

    def __str__(self):
        return f'{self.location_id} - {self.description}'


class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='items', default='items/no_photo.jpg')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class Clue(models.Model):
    crime_id = models.ForeignKey(CrimeSceneReport, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=500, default=None)
    
    class Meta:
        verbose_name = 'Clue'
        verbose_name_plural = 'Clues'

    def __str__(self):
        return f'{self.crime_id}-{self.item_id}'


class Airports(models.Model):
    full_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'

    def __str__(self):
        return self.full_name


class Flights(models.Model):
    origin_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='departing_flights')
    destination_airport_id = models.ForeignKey(Airports, on_delete=models.CASCADE, related_name='arriving_flights')
    date = models.DateField()
    time = models.TimeField()
    type = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    def __str__(self):
        return f'{self.origin_airport_id} - {self.destination_airport_id} -{self.date}'


class Passengers(models.Model):
    flight_id = models.ForeignKey(Flights, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    seat = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'

    def __str__(self):
        return f'{self.flight_id} - {self.person_id}'


class Interviews(models.Model):
    name = models.CharField(max_length=200)
    transcript = models.CharField(max_length=500)
    street_id = models.ForeignKey(Street, on_delete=models.CASCADE, default=None)
    date = models.DateField()

    class Meta:
        verbose_name = 'Interview'
        verbose_name_plural = 'Interviews'

    def __str__(self):
        return f'{self.name} - {self.street_id}'


class MessageBox(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    date = models.DateField()

    class Meta:
        verbose_name = 'Message Box'
        verbose_name_plural = 'Message Boxes'

    def __str__(self):
        return f'{self.person_id} - {self.body}'


class PlayerReply(models.Model):
    message_id = models.ForeignKey(MessageBox, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Player Reply'
        verbose_name_plural = 'Player Replies'

    def __str__(self):
        return self.message_id


class NpcReply(models.Model):
    PlayerReply_id = models.ForeignKey(PlayerReply, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Npc Reply'
        verbose_name_plural = 'Npc Replies'

    def __str__(self):
        return self.PlayerReply_id
