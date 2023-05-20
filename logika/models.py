from django.db import models
import uuid

# Create your models here.


class Foydalanuvchi(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    isim = models.CharField(blank=True, null=True, max_length=50)
    key = models.CharField(blank=True, null=True, max_length=50)

# Create your models here.
