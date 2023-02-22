from django.db import models


class Categoria (models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField()

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Transações"
