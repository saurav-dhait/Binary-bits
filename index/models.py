from django.db import models
import uuid


class Agency(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    address = models.TextField(blank=False)
    type_of_agency = models.CharField(blank=False, max_length=200)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique=True, blank=False)
