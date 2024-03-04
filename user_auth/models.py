import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    agency_id = models.CharField(unique=True, max_length=10, null=False, blank=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.agency_id}"
