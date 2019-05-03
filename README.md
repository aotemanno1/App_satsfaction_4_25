# App_satsfaction_4_25
Can run properly, and load the data.

del db.sqlite3
py manage.py makemigrations
py manage.py migrate --run-syncdb
py manage.py load_app_data
py manage.py runserver
