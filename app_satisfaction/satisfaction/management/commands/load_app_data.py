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
        # os.system("del db.sqlite3")
        if Feedback.objects.exists():
            print('Data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        # for row in DictReader(open('C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv')):
        path_to_file = "C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv"
        # path_to_file = "C:\\python37\\Scripts\\myScripts\\Beta_Feedback\\Apps2Beta1.csv"
        data = pd.read_csv(path_to_file)
        name = data['First L. Name']

        score_list = ['Hub Satisfaction', 'Calendar Satisfaction',
                      'Contacts Satisfaction', 'Tasks Satisfaction', 'Notes Satisfaction']
        for app in score_list:
            data[app].replace(float('NaN'), -1, inplace=True)

        comment_list = ['Hub Comments', 'Calendar Comments', 'Contacts Comments', 'Tasks Comments', 'Notes Comments']
        for app in comment_list:
            data[app].replace(float('NaN'), '', inplace=True)

        for index in range(0, name.size):
            feedback = Feedback()
            feedback.submitter = data['First L. Name'][index]
            feedback.email = data['Email Address'][index]
            feedback.score_hub = data['Hub Satisfaction'][index]
            feedback.comment_hub = data['Hub Comments'][index]
            feedback.score_calendar = data['Calendar Satisfaction'][index]
            feedback.comment_calendar = data['Calendar Comments'][index]
            feedback.score_contacts = data['Contacts Satisfaction'][index]
            feedback.comment_contacts = data['Contacts Comments'][index]
            feedback.score_tasks = data['Tasks Satisfaction'][index]
            feedback.comment_tasks = data['Tasks Comments'][index]
            feedback.score_notes = data['Notes Satisfaction'][index]
            feedback.comment_notes = data['Notes Comments'][index]
            feedback.save()

        print('name finished')

        if Fruit.objects.exists():
            print('Data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        for row in DictReader(open('./fruit_data.csv')):
            fruit = Fruit()
            fruit.name = row['name']
            fruit.amt = row['amt']
            fruit.save()



