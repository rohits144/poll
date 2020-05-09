from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Questions(models.Model):
    """
    This class creates a model/table for questions
    """
    question = models.CharField(max_length=500, blank=False, unique=True)
    enabled = models.BooleanField(default=False, editable=True)
    upvotes = models.IntegerField(default=0, editable=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.TimeField(auto_now_add=True)
    total_num_of_options = models.IntegerField(blank=True, default=0)
    last_updated_time = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ["-creation_time"]

    def __str__(self):
        return self.question


class Options(models.Model):
    statement = models.CharField(max_length=200, default="option statement", editable=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    creation_time = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_time = models.TimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_time"]
        unique_together = ("statement", "question",)

    def __str__(self):
        return self.statement


def update_options_number_in_question(sender, instance, created, **kwargs):
    question = instance.question
    question.enabled = True
    question.total_num_of_options = len(question.options_set.all())
    question.save()


post_save.connect(receiver=update_options_number_in_question, sender=Options)
