"""
Command to wait for the database to be available.
"""
import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as PgOperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """Entrypoint for the command"""
        self.stdout.write('Waiting for database...')
        db_up = None

        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, PgOperationalError):
                self.stdout.write('Database unavailable, waiting...')
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS('Database available'))
