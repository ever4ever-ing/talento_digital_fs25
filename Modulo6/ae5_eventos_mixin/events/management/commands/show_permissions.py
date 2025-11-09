from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Mostrar permisos en auth_permission para la app events'

    def handle(self, *args, **options):
        perms = Permission.objects.filter(content_type__app_label='events')
        for p in perms:
            self.stdout.write(f"{p.id}: {p.content_type.app_label}.{p.codename} - {p.name}")
