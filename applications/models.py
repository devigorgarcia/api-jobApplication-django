from django.db import models
import uuid
# Create your models here.


class LevelOptions(models.TextChoices):
    JUNIOR = "Junior"
    PLENO = "Pleno"
    SENIOR = "Senior"


class DevelopOptions(models.TextChoices):
    FRONT_END = 'Front-end'
    BACK_END = 'Back-end'
    FULL_STACK = 'Full-stack'


class Application(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    obs = models.TextField(max_length=50)
    level = models.CharField(max_length=50, choices=LevelOptions.choices)
    develop = models.CharField(max_length=50, choices=DevelopOptions.choices)
    register_date = models.DateTimeField(auto_now_add=True)

    # FK
    user = models.ForeignKey(
        "users.User", related_name="applications", on_delete=models.CASCADE)

    status = models.ManyToManyField(
        "status.Status", related_name="applications", blank=True)

    stacks = models.ManyToManyField(
        "stacks.Stack", related_name="applications", blank=True)
