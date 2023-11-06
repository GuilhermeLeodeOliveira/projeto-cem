from django.db import models
from core.models import Docente, PosDout, AlunoPosIC, UserExterno
from equipamentos.models import Equipamento
# Create your models here.

class Solicitacoes(models.Model):
    id_solicitacao = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=50)
    id_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE, blank=True, null=True)
    id_PosDout = models.ForeignKey(PosDout, on_delete=models.CASCADE, blank=True, null=True)
    id_AlunoPosIC = models.ForeignKey(AlunoPosIC, on_delete=models.CASCADE, blank=True, null=True)
    id_UserExterno = models.ForeignKey(UserExterno, on_delete=models.CASCADE, blank=True, null=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, blank=False, null=False)
    
    def __str__(self):
        return self.status