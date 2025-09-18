from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking  # Booking from bookings app


# -------------------------
# Tool model
# -------------------------
class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# -------------------------
# Equipment models
# -------------------------
class Tractor(models.Model):
    name = models.CharField(max_length=100, default="Tractor")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Plough(models.Model):
    name = models.CharField(max_length=100, default="Plough")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class WaterPump(models.Model):
    name = models.CharField(max_length=100, default="WaterPump")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Drone(models.Model):
    name = models.CharField(max_length=100, default="Drone")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Harrow(models.Model):
    name = models.CharField(max_length=100, default="Harrow")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Loader(models.Model):
    name = models.CharField(max_length=100, default="Loader")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Seeder(models.Model):
    name = models.CharField(max_length=100, default="Seeder")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Sprayer(models.Model):
    name = models.CharField(max_length=100, default="Sprayer")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Wagon(models.Model):
    name = models.CharField(max_length=100, default="Wagon")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Plows(models.Model):
    name = models.CharField(max_length=100, default="Plows")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Baler(models.Model):
    name = models.CharField(max_length=100, default="Baler")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Harvester(models.Model):
    name = models.CharField(max_length=100, default="Harvester")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


# -------------------------
# Payment model
# -------------------------
class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Completed", "Completed"),
            ("Failed", "Failed"),
        ],
        default="Pending"
    )

    def __str__(self):
        return f"Payment for {self.booking} - {self.status}"
