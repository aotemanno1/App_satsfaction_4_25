# reference for charts: https://hackernoon.com/server-rendered-charts-in-django-2604f903389d

import pygal
import sqlite3
import os

from .models import Fruit, Feedback



class FruitPieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Amount of Fruits'

    def get_data(self):
        '''
        Query the db for chart data, pack them into a dict and return it.
        '''
        data = {}
        for fruit in Fruit.objects.all():
            data[fruit.name] = fruit.amt
        return data

    def generate(self):
        # Get chart data
        chart_data = self.get_data()

        # Add data to chart
        for key, value in chart_data.items():
            self.chart.add(key, value)

        # Return the rendered SVG
        return self.chart.render(is_unicode=True)


class ScorePieChart():

    def __init__(self, **kwargs):
        self.chart = pygal.Pie(**kwargs)
        self.chart.title = 'Score Distribution'

    def get_data(self, app):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_hub <= 5''')
        low = c.fetchall()[0][0]
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_hub >= 6 AND score_hub <= 7''')
        mid = c.fetchall()[0][0]
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_hub >= 8''')
        high = c.fetchall()[0][0]

        data = {}
        data['0~5'] = int(low)
        data['6~7'] = int(mid)
        data['8~10'] = int(high)
        return data

    def generate(self):
        chart_data = self.get_data()

        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)
