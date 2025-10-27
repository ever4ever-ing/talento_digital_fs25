from django.urls import path
from django.utils.module_loading import import_string

app_name = 'recetas'

def lazy_view(dotted_path):
    def _view(request, *args, **kwargs):
        view = import_string(dotted_path)
        return view(request, *args, **kwargs)
    return _view

urlpatterns = [
    path('', lazy_view('recetas.views.lista_recetas'), name='mis_recetas'),
    path('<int:receta_id>/', lazy_view('recetas.views.detalle_receta'), name='detalle_receta'),
]