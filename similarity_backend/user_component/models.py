from django.db import models
from django.contrib.auth.models import User

# https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
# https://learndjango.com/tutorials/django-best-practices-referencing-user-model

class UserHistory(models.Model):
    model_utilized = models.CharField(max_length=50)
    transaction_charge = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)