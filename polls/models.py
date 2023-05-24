from django.db import models
import datetime
from django.contrib import admin

from django.db import models
from django.utils import timezone

class Question(models.Model): # First class is a model being created called Questions
    question_text = models.CharField(max_length = 200) # Contains the question being asked
    pub_date = models.DateTimeField("date published") # Contains the publication date
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now    

class Choice(models.Model): # Second class is the choice
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200) # Contains the text for the choices
    votes = models.IntegerField(default = 0) # Contains the number of votes
    def __str__(self):
        return self.choice_text
# Create your models here.
