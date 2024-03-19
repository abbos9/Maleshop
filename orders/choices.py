from django.db import models

class Status_Choices(models.TextChoices):
    pending = 'pending', "Pending"
    cancelled = 'cancelled', "Cancelled"
    completed = 'completed', "Completed"
    