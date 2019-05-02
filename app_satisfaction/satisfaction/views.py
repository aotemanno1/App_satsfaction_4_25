import sqlite3


from django.shortcuts import render
from pygal.style import DarkStyle
from .models import Feedback, Fruit
from .charts import FruitPieChart, ScorePieChart


def home(request):
    return render(request, 'home.html')


def hub_list(request):
    feedbacks = Feedback.objects.all()

    cht_score = ScorePieChart(
        height=600,
        width=800,
        explicit_size=True,
        style=DarkStyle
    )
    cht_score_hub = cht_score.generate('''hub''')

    dict_score = {'cht_score_hub': cht_score_hub}
    return render(request, 'hub_list.html', dict_score)
    # return render(request, 'hub_list.html')


def calendar_list(request):
    cht_score = ScorePieChart(
        height=600,
        width=800,
        explicit_size=True,
        style=DarkStyle
    )
    cht_score_calendar = cht_score.generate('''calendar''')
    dict_score = {'cht_score_calendar': cht_score_calendar}
    return render(request, 'calendar_list.html', dict_score)
    # return render(request, 'calendar_list.html')


def hub_detail(request, id):
    feedback = Feedback.objects.get(id=id)
    return render(request, 'hub_detail.html', {'feedback': feedback})


def hub_score_0_5(request):
    feedbacks = Feedback.objects.all()
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


