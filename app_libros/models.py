from django.db import models
from datetime import date

class Libros(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    subido_por_id = models.ForeignKey('login_app.Usuario', related_name="libro_subido", on_delete=models.CASCADE, null=True)
    le_gusta = models.ManyToManyField('login_app.Usuario', related_name="libro_favorito")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
