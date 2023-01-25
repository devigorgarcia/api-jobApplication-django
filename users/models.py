from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    email = models.CharField(max_length=127)
    password = models.CharField(max_length=127)
