from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from events.views import logout_view, CustomLoginView
from django.conf.urls import handler404
from events import views as events_views
# config/urls.py (antes de la ruta de login)
from django.views.generic import RedirectView

def root(request):
    return redirect('events:list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('events/', include('events.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    # redirigir cualquier /login/<algo> a /login/
    path('login/<path:any>/', RedirectView.as_view(url='/login/', permanent=False)),
]
