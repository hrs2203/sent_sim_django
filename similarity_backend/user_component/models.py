from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UserHistory(models.Model):
    """
    ## UserHistory
    for storing UserHistory
    - Fields
        - user_id : Foreign Key to User Model, on_delete: CASCADE
        - model_utilized : name of model used
        - transaction_charge : total charge for operation
        - quert_count : total number of queries in the transaction.   
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    model_utilized = models.CharField(max_length=50)
    transaction_charge = models.IntegerField()
    quert_count = models.IntegerField(default=1)


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


class SemanticModel(models.Model):
    """
    ## SemanticModel
    for storing SemanticModel
    - Fields
        - model_name : model name ( unique )
        - charge : charge per query ( per embedding generation )
    """
    model_name = models.CharField(max_length=20)
    charge = models.IntegerField(default=10)


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
