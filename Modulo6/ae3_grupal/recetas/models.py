from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
    
    def __str__(self):
        return self.nombre
    
    def get_descripcion_corta(self):
        """Retorna los primeros 100 caracteres de los ingredientes como descripción"""
        return self.ingredientes[:100] + '...' if len(self.ingredientes) > 100 else self.ingredientes
