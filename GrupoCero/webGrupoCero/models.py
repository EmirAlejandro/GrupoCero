from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='foto',null=True)
    
    def __str__(self) -> str:
        return super().__str__()

class Obra(models.Model):
    idObra = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=45)
    creacion=models.IntegerField()
    descripcion=models.TextField()
    foto = models.ImageField(upload_to='foto',null=True)
    publicar=models.BooleanField(default=False)
    comentario=models.TextField(default='--')
    usuario=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
