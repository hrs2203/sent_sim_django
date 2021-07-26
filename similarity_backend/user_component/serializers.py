from rest_framework import serializers
from user_component.models import (
    User, UserHistory, UserDetails, SemanticModel, QueryModel
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = '__all__'


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'


class SemanticModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemanticModel
        fields = '__all__'


class QueryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryModel
        fields = '__all__'
