from django.contrib import admin

from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['submitter', 'email', 'score_hub', 'comment_hub']
