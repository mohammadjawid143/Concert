from django.db import models
from accounts.models import User
from ticketSales.models import timeModel, concertModel
from datetime import datetime


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    is_paid = models.BooleanField(default=False, verbose_name="Paid/Unpaid")
    payment_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Order for {self.user.username} - {'Paid' if self.is_paid else 'Pending'}"

    @property
    def total_price(self):
        return sum(detail.final_price for detail in self.details.all())


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="details")
    concert = models.ForeignKey(concertModel, on_delete=models.PROTECT,
                                related_name="order_details")
    seats = models.ForeignKey(
        timeModel,
        on_delete=models.PROTECT,
        related_name="order_details",
        null=True,
        blank=True
    )
    seat_count = models.PositiveIntegerField(default=1, null=True, blank=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if self.concert and self.seat_count:
            self.final_price = self.seat_count * self.concert.price
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order)
