from django.db import models


class Feedback(models.Model):
    submitter = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    score_hub = models.IntegerField(null=True, blank=True)
    # score_hub = models.CharField(max_length=100, null=True, blank=True)
    comment_hub = models.TextField(null=True, blank=True)

    score_calendar = models.CharField(max_length=100, null=True, blank=True)
    comment_calendar = models.TextField(null=True, blank=True)

    score_contacts = models.CharField(max_length=100, null=True, blank=True)
    comment_contacts = models.TextField(null=True, blank=True)

    score_tasks = models.CharField(max_length=100, null=True, blank=True)
    comment_tasks = models.TextField(null=True, blank=True)

    score_notes = models.CharField(max_length=100, null=True, blank=True)
    comment_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.submitter


class Fruit(models.Model):
    name = models.CharField(max_length=255)
    amt = models.IntegerField()

    def __str__(self):
        return self.name

