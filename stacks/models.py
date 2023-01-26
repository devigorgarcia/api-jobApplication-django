from django.db import models
import uuid
# Create your models here.


class Stack(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stack = models.CharField(max_length=50)
