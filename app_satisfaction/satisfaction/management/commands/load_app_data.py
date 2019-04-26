from csv import DictReader

from django.core.management import BaseCommand

from satisfaction.models import Feedback, Fruit

import pandas as pd



ALREADY_LOADED_ERROR_MESSAGE = """
----->>manage.py migrate --run-syncdb<<-----stupid command
If you need to reload the app data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from app_data.csv into our Feedback model"

    def handle(self, *args, **options):
        if Feedback.objects.exists():
            print('Data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        # for row in DictReader(open('C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv')):
        # path_to_file = "C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv"
        path_to_file = "C:\\python37\\Scripts\\myScripts\\Beta_Feedback\\Apps2Beta1.csv"
        data = pd.read_csv(path_to_file, encoding='utf-8')
        data = data.fillna(-1)
        col = ['First L. Name', 'Email Address', 'Hub Satisfaction', 'Hub Comments',
                    'Calendar Satisfaction', 'Calendar Comments', 'Contacts Satisfaction',
                    'Contacts Comments', 'Tasks Satisfaction', 'Tasks Comments',
                    'Notes Satisfaction', 'Notes Comments']

        for row in data['Email Address']:
            feedback = Feedback()
            feedback.email = row
            feedback.save()
        for row in data['First L. Name']:
            feedback = Feedback()
            feedback.submitter = row
            feedback.save()

        # count = 0
        # for each_col in col:
        #     each_col_data = data[each_col]
        #     count += 1
        #     for row in each_col_data:
        #         if count == 1:
        #             feedback = Feedback()
        #             feedback.submitter = row
        #             feedback.save()
        #         elif count == 2:
        #             feedback = Feedback()
        #             feedback.email = row
        #             feedback.save()
        #     break

        if Fruit.objects.exists():
            print('Data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(open('./fruit_data.csv')):
            fruit = Fruit()
            fruit.name = row['name']
            fruit.amt = row['amt']
            fruit.save()



