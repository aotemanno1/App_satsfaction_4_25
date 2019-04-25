from csv import DictReader

from django.core.management import BaseCommand

from satisfaction.models import Fruit


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the app data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from app_data.csv into our Feedback model"

    def handle(self, *args, **options):
        if Fruit.objects.exists():
            print('App data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(open('./fruit_data.csv')):
            fruit = Fruit()
            fruit.name = row['name']
            fruit.amt = row['amt']
            fruit.save()



