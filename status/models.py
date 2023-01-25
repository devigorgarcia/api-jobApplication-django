from django.db import models
import uuid
# Create your models here.


class StatusOptions(models.TextChoices):
    CV = 'Analise de CV',
    FIT = 'Teste Fit Cultural',
    TESTE = 'Teste Técnico',
    RH = 'Entrevista RH',
    TECNICO = 'Entrevista Técnica',
    CONTRATADO = 'Contratado',
    RECUSADO = 'Recusado',


class Status(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    status = models.CharField(max_length=50, choices=StatusOptions.choices)
