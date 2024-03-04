import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from index.models import Agency


class MyUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    email = models.EmailField(unique=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username}"
