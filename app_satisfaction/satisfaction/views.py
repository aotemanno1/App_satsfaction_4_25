import sqlite3


from django.shortcuts import render
from pygal.style import DarkStyle
from .models import Feedback, Fruit
from .charts import FruitPieChart, ScorePieChart


def home(request):
    return render(request, 'home.html')


def hub_list(request, app):
    cht_score = ScorePieChart()
    cht_score_hub = cht_score.generate('''%s''' % app)
    dict_score = {'cht_score_hub': cht_score_hub}
    html_file = app + '_list.html'
    return render(request, html_file, dict_score)


def hub_detail(request, id):
    feedback = Feedback.objects.get(id=id)
    return render(request, 'hub_detail.html', {'feedback': feedback})


def hub_score_0_5(request):
    feedbacks = Feedback.objects.all()
    # return render(request, 'hub_score_0_5.html', {'feedbacks': feedbacks, 'app': app})
    return render(request, 'hub_score_0_5.html', {'feedbacks': feedbacks})


def hub_score_6_8(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'hub_score_6_8.html', {'feedbacks': feedbacks})


def hub_score_9_10(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'hub_score_9_10.html', {'feedbacks': feedbacks})


def calendar_score_0_5(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'calendar_score_0_5.html', {'feedbacks': feedbacks})


def calendar_score_6_8(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'calendar_score_6_8.html', {'feedbacks': feedbacks})


def calendar_score_9_10(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'calendar_score_9_10.html', {'feedbacks': feedbacks})


def fruit(request):
    cht_fruits = FruitPieChart(
        height=600,
        width=800,
        explicit_size=True,
        style=DarkStyle
    )
    cht_fruits = cht_fruits.generate()
    return render(request, 'fruit.html', {'cht_fruits': cht_fruits})


def test(request):
    cht_score = ScorePieChart(
        height=600,
        width=800,
        explicit_size=True,
        style=DarkStyle
    )
    cht_score = cht_score.generate()
    # cht_score = ScorePieChart().generate()

    return render(request, 'test.html', {'number': cht_score})


