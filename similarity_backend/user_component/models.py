from django.db import models
from django.contrib.auth.models import User, UserManager


class UserHistory(models.Model):
    """
    ## UserHistory
    for storing UserHistory
    - Fields
        - user_id : Foreign Key to User Model, on_delete: CASCADE
        - model_utilized : name of model used
        - transaction_charge : total charge for operation
        - query_count : total number of queries in the transaction.   
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_charge = models.IntegerField(default=0)
    query_count = models.IntegerField(default=1)
    credit_added = models.BooleanField(default=False)
    comp_type = models.CharField(max_length=200, default="CUSTOM") # other is DB


class HistorySentence(models.Model):
    """Sentences sent by api for comparision"""
    sentence = models.CharField(
        max_length=500, default="Sentence Not Available"
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    history_id = models.ForeignKey(UserHistory, on_delete=models.CASCADE)


class UserDetail(models.Model):
    """
    ## UserDetail
    for storing UserDetail
    - Fields
        - user_id : Foreign Key to User Model, on_delete: CASCADE
        - total_credits : total credit left in user account
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_credits = models.IntegerField(default=100)
    saved_query_file = models.CharField(max_length=200, default="")


class QueryModel(models.Model):
    """
    ## QueryModel
    for storing QueryModel
    - Fields
        - user_id : Foreign Key to User Model, on_delete: CASCADE
        - query : the query to store. eg. "how to save money in subscription"
        - query_response : the response for this query. eg. "Try our student package"
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=100)
    query_response = models.CharField(max_length=100)

