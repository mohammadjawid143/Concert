from django.db import models
from accounts.models import User
# Create your models here.


class concertModel(models.Model):
    name = models.CharField(max_length=100)
    SingarName = models.CharField(max_length=100)
    lenth = models.IntegerField()
    poster = models.ImageField(upload_to="concertImage/")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=100.00)

    def __str__(self):
        return self.SingarName


class locationModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=11)
    capcity = models.IntegerField()

    def __str__(self):
        return self.name


class timeModel(models.Model):
    concertModel = models.ForeignKey("concertModel", on_delete=models.PROTECT)
    locationModel = models.ForeignKey("locationModel", on_delete=models.PROTECT)
    StartDateTime = models.DateTimeField()
    Seats = models.IntegerField()
    remaining_seats = models.IntegerField(default=0)

    Start = 1
    End = 2
    Cancel = 3
    Solled = 4

    status_choices = (
        (Start, "Selling ticket Start"),
        (End, "Selling ticket Ended"),
        (Cancel, "This Sance Canceled"),
        (Solled, "Ticket Selling is open")
    )

    status = models.IntegerField(choices=status_choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.remaining_seats = self.Seats
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.concertModel} at {self.locationModel} on {self.StartDateTime}"


class ticketModels(models.Model):
    ProfileModel = models.ForeignKey(User, on_delete=models.PROTECT)
    timeModel = models.ForeignKey("timeModel", on_delete=models.PROTECT)

    tecketImage = models.ImageField(upload_to="ticketimages/")

    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"Ticket_info: Profile: {self.ProfileModel} Concert_Info: {User.__str__(), timeModel.__str__()}"
