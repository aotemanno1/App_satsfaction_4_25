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


import pandas as pd
path_to_file = "C:\\Users\\wenjli\\Desktop\\Apps2Beta1.csv"
data = pd.read_csv(path_to_file, encoding='utf-8')
data = data.fillna(-1)
name = data[['First L. Name', 'Email Address']]
i = 1
for row in name:
    print(row)
    # print(i)
    # i += 1
    # break

