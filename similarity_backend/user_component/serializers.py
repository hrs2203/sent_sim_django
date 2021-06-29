from rest_framework import serializers
from .models import UserHistory, User


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserHistorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = '__all__'