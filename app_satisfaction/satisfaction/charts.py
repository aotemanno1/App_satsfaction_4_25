# reference for charts: https://hackernoon.com/server-rendered-charts-in-django-2604f903389d

import pygal
import sqlite3
from pygal.style import DarkStyle

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

        self.height = 600
        self.width = 800,
        self.explicit_size = True,
        # self.style = 'DarkStyle'
        self.style = DarkStyle

    def get_data(self, app):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_%s <= 5 AND score_%s >= 0''' % (app, app))
        low = c.fetchall()[0][0]
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_%s >= 6 AND score_%s <= 7''' % (app, app))
        mid = c.fetchall()[0][0]
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_%s >= 8''' % app)
        high = c.fetchall()[0][0]
        c.execute('''SELECT COUNT(id) FROM satisfaction_feedback WHERE score_%s == -1''' % app)
        others = c.fetchall()[0][0]

        data = {}
        data['0~5'] = int(low)
        data['6~7'] = int(mid)
        data['8~10'] = int(high)
        data['others'] = int(others)
        return data

    def generate(self, app):
        chart_data = self.get_data(app)

        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)
