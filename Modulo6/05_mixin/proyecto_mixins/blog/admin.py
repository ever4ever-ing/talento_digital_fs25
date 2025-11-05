from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para Post
    """
    list_display = ('titulo', 'autor')
    list_filter = ('autor',)
    search_fields = ('titulo', 'contenido')
