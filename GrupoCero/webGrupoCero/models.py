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
    precio = models.IntegerField(default=100)
    
    def __str__(self):
        return self.nombre
    
    
class Galeria(models.Model):
    idFoto= models.AutoField(primary_key=True)
    foto= models.ImageField(upload_to='foto',null=True)
    obra= models.ForeignKey(Obra,on_delete=models.CASCADE)

    
    def __str__(self) -> str :
        return str(self.idFoto)+ " "+str(self.obra.nombre)


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    obras = models.ManyToManyField(Obra)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra del usuario {self.usuario.username} - Total: ${self.total}"