# import sqlite3
#
# conn = sqlite3.connect('db.sqlite3')
# c = conn.cursor()
# c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score<=5''')
# number = c.fetchall()[0][0]


from csv import DictReader

# for row in DictReader(open('C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv')):
#     print(row['Email Address'])
#     # print(row['Hub Satisfaction'])
#     break

import numpy
import pandas as pd
# path_to_file = "C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv"
path_to_file = "C:\\python37\\Scripts\\myScripts\\Beta_Feedback\\Apps2Beta1.csv"
data = pd.read_csv(path_to_file, encoding='utf-8')
test = data['Hub Satisfaction'].fillna(-1)
# name = data['First L. Name']
# i = 1
# for row in name:
#     print(row)
    # print(i)
    # i += 1
    # break

