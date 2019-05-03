"""app_satisfaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from satisfaction import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^hub_list/', views.hub_list, name='hub_list'),
    url(r'^hub_detail/(\d+)/', views.hub_detail, name='hub_detail'),
    url(r'^hub_score_0_5', views.hub_score_0_5, name='hub_score_0_5'),
    url(r'^hub_score_6_8', views.hub_score_6_8, name='hub_score_6_8'),
    url(r'^hub_score_9_10', views.hub_score_9_10, name='hub_score_9_10'),

    url(r'^calendar_list/', views.calendar_list, name='calendar_list'),
    url(r'^calendar_score_0_5', views.calendar_score_0_5, name='calendar_score_0_5'),
    url(r'^calendar_score_6_8', views.calendar_score_6_8, name='calendar_score_6_8'),
    url(r'^calendar_score_9_10', views.calendar_score_9_10, name='calendar_score_9_10'),

    url(r'^contacts_list/', views.contacts_list, name='contacts_list'),
    url(r'^tasks_list/', views.tasks_list, name='tasks_list'),
    url(r'^notes_list/', views.notes_list, name='notes_list'),

    url(r'^fruit', views.fruit, name='fruit'),
    url(r'^test', views.test, name='test'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
