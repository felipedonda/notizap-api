from django.db import models
from django.contrib.auth.models import User
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    timezone = models.CharField(max_length=50)

class Reminder(models.Model):
    FREQUENCY_CHOICES = [
        ("none", "None"),
        ("daily", "Daily"),
        ("weekly", "Weekly"),
        ("monthly", "Monthly"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    minutes_prior = models.IntegerField(default=0)
    scheduled_time = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    remind_daybefore = models.BooleanField(default=False)
    is_task = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False)
    frequency =  models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default="none")
    frequency_skips = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        phone_number = self.user.userprofile.phone_number
        recurring_str = f" ({self.frequency})" if self.recurring else ""
        type_str = "Reminder" if not self.is_task else "Task"
        done_str = " (done)" if self.done else " (pending)"
        done_str = done_str if self.is_task else ""
        return f"{type_str}: {self.title}{recurring_str} - {self.scheduled_time}{done_str} for {self.user.email} at {phone_number}."
