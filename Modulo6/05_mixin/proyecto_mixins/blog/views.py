from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import Post

# Vista pública
class ListaPosts(ListView):
    model = Post
    template_name = 'blog/lista_posts.html'
    context_object_name = 'posts'

# Vista privada (solo usuarios autenticados)
class MisPosts(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/mis_posts.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        # Solo muestra posts del usuario logueado
        return Post.objects.filter(autor=self.request.user)

# Vista con permiso (editar posts)
class EditarPost(PermissionRequiredMixin, TemplateView):
    template_name = 'blog/editar_post.html'
    permission_required = 'blog.change_post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['usuario'] = self.request.user
        return context