from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Booked", "Booked"),
        ("Cancelled", "Cancelled"),
        ("Completed", "Completed"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tool = models.ForeignKey('dashboard_app.Tool', on_delete=models.CASCADE)  # 👈 string reference avoids circular import
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.tool.name} ({self.status})"
