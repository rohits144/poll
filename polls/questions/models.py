from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    """
    This class creates a model/table for questions
    """
    question = models.CharField(max_length= 500)
    upvotes = models.IntegerField(default=0, editable=True)
    options = dict()
    created_by = models.ForeignKey(User,on_delete=None)
    creation_time = models.TimeField()
    last_updated_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.question, self.upvotes, self.creation_time