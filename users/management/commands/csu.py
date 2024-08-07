import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            tg_chat_id=os.getenv('TG_CHAT_ID')
        )
        user.set_password('admin')
        user.save()
        print('SuperUser created')
