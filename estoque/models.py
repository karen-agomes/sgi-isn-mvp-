from datetime import date
from django.db import models

class Beneficiario(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)

class Insumo(models.Model):
    nome = models.CharField(max_length=150)
    quantidade = models.PositiveIntegerField(default=0)
    data_validade = models.DateField()

    def status_validade(self):
        dias = (self.data_validade - date.today()).days
        if dias <= 5:
            return "CRÍTICO"
        elif dias <= 15:
            return "ATENÇÃO"
        return "OK"
