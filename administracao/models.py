from django.db import models

# Create your models here.
class Adm(models.Model):
    id_adm = models.AutoField(primary_key=True)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.email