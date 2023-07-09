"""
Django command to wait for the database to be available.
"""
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """
    Django command to wait for the database to be available.
    """

    def handle(self, *args, **options):
        """Endpoint for the command"""

        self.stdout.write('Waiting for db')
        db_not_up = True
        while db_not_up:
            try:
                self.check(databases=['default'])
                db_not_up = False
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second.')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
