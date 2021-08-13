""" Django Model Utils for Read and Write Operations """

from django.db import transaction

from user_component.models import (
    User, UserHistory, UserDetail, SemanticModel, QueryModel
)

from user_component.serializers import (
    UserSerializer, UserHistorySerializer, UserDetailSerializer, 
    SemanticModelSerializer, QueryModelSerializer
)

SAMPLE = "HRISHABH"