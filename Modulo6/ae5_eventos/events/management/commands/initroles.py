from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps


class Command(BaseCommand):
    help = 'Crear grupos: admins, organizers, attendees y asignar permisos para Event'

    def handle(self, *args, **options):
        Event = apps.get_model('events', 'Event')
        perms = Permission.objects.filter(content_type__app_label='events')

        admins, _ = Group.objects.get_or_create(name='admins')
        organizers, _ = Group.objects.get_or_create(name='organizers')
        attendees, _ = Group.objects.get_or_create(name='attendees')

        # admins: todos los permisos de events
        admins.permissions.set(perms)

        # organizers: add & change but not delete
        organizer_perms = perms.filter(codename__in=['add_event', 'change_event', 'can_manage_event'])
        organizers.permissions.set(organizer_perms)

        # attendees: no permisos de modificación
        attendees.permissions.clear()

        self.stdout.write(self.style.SUCCESS('Grupos inicializados'))
