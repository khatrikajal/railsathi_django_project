from django.db import models

class PassengerComplaint(models.Model):
    passenger_name = models.CharField(
        max_length=100,
        verbose_name="Passenger Name"
    )
    user_phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name="Phone Number"
    )
    train_no = models.CharField(
        max_length=10,
        verbose_name="Train Number"
    )
    train_name = models.CharField(
        max_length=100,
        verbose_name="Train Name"
    )
    start_date_of_journey = models.DateField(
        verbose_name="Journey Start Date"
    )
    coach = models.CharField(
        max_length=10,
        verbose_name="Coach Number",
        blank=True
    )
    berth = models.CharField(
        max_length=10,
        verbose_name="Berth Number",
        blank=True
    )
    pnr = models.CharField(
        max_length=20,
        verbose_name="PNR Number",
        blank=True
    )
    description = models.TextField(
        verbose_name="Complaint Description"
    )
    train_depo = models.CharField(
        max_length=100,
        verbose_name="Train Depot"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )

    class Meta:
        verbose_name = "Passenger Complaint"
        verbose_name_plural = "Passenger Complaints"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.passenger_name} | {self.train_no} | {self.pnr}"
