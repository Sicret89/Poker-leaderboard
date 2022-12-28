"""
Django command to wait for the database to be available.
"""
# from django.db.models.loading import get_model
import csv
import time

from api.models import SingleTournament
from django.core.management.base import BaseCommand

# try:
#     from django.db.models.loading import get_model
# except ImportError:
#     from django.apps import apps
#
#     get_model = apps.get_model


class Command(BaseCommand):
    """Django command to import csv file."""

    help = "Load a questions csv file into the database"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str)

    def handle(self, *args, **kwargs):
        path = kwargs["path"]
        with open(path, "rt") as f:
            reader = csv.reader(f, dialect="excel")
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    _, created = SingleTournament.objects.get_or_create(
                        player=row[0],
                        points=row[1],
                        bonus_a=row[2],
                        bonus_b=row[3],
                    )
