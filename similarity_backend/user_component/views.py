import re
from user_component.models import User, UserDetail, UserHistory
from user_component.serializers import UserDetailSerializer, UserSerializer, UserHistorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_component.comparision_engine import MultiSentenceBertComparision

from user_component.static_var import QUERY_CHARGE


class FuzzyAPIView(APIView):
    """User class default api view providing default functions as needed"""

    INVALID_VALUE = "invalid input"
    DEFAULT_CHARGE = 10

    def get_all_user(self):
        return User.objects.all()

    def get_user(self, pk: int):
        data = None
        try:
            data = User.objects.get(id=pk)
        except:
            data = None
        return data

    def get_user_detail(self, pk: int):
        user_obj = self.get_user(pk)
        if user_obj:
            try:
                user_detail_obj = UserDetail.objects.get(user_id=user_obj)
                return user_detail_obj
            except:
                return None
        return None

    def get_user_email(self, email: str):
        data = None
        try:
            data = User.objects.get(email=email)
        except:
            data = None
        return data

    def create_new_user(self, username: str, email: str, password: str):
        """ create unique user by email ? if present, returns from db"""
        check_user = self.get_user_email(email)
        if check_user == None:
            try:
                newUser = User(
                    username=username,
                    email=email,
                    password=password
                )
                newUser.set_password(password)
                newUser.save()
                newUserBank = UserDetail(user_id=newUser)
                newUserBank.save()
                return newUser
            except:
                return None
        return check_user

    def add_credit_to_user(self, pk, amt):
        user_obj = self.get_user_detail(pk)
        if user_obj == None:
            return False
        try:
            user_obj.total_credits += amt
            user_obj.save()
            return True
        except:
            return False

    def get_user_history(self, pk: int):
        """ Get user history by user id """
        data = []
        try:
            data = UserHistory.objects.filter(user_id=pk)
        except:
            pass
        return data

    def create_new_user_history(
        self, transaction_charge: str, user_id: int
    ):
        user_obj = self.get_user(user_id)
        if user_obj == None:
            return None
        try:
            newUserHistory = UserHistory(
                transaction_charge=transaction_charge,
                query_count=(transaction_charge//QUERY_CHARGE),
                user_id=user_obj
            )
            newUserHistory.save()
            return True
        except:
            return False

    def get_transaction_charge(self):
        return QUERY_CHARGE

    def get_invalid_message(self, msg=None):
        msg = msg or "invalid input"
        return {"statue": status.HTTP_400_BAD_REQUEST, "data": msg}

    def get_valid_message_body(self, body=None):
        body = body or {}
        return {"statue": status.HTTP_200_OK, "data": body}

    def validate_input(self, *args):
        "Validate that no entry is false"
        for item in args:
            if item == None:
                return False
        return True


class LoginUser(FuzzyAPIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not self.validate_input(email, password):
            return Response(self.get_invalid_message())

        user_object = self.get_user_email(email=email)
        if user_object == None:
            return Response(self.get_invalid_message(self.INVALID_VALUE))
        if not user_object.check_password(password):
            return Response(self.get_invalid_message("Invalid Password"))
        UserSerialized = UserSerializer(user_object)
        return Response(self.get_valid_message_body(UserSerialized.data))


class RegisterUser(FuzzyAPIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        username = request.data.get('username', None)

        if not self.validate_input(email, password, username):
            return Response(self.get_invalid_message())

        newuser = self.create_new_user(username, email, password)
        UserSerialized = UserSerializer(newuser)
        return Response(self.get_valid_message_body(UserSerialized.data))


class UserAmount(FuzzyAPIView):
    def get(self, request, pk, amt):
        if not self.validate_input(pk, amt):
            return Response(self.get_invalid_message())
        self.add_credit_to_user(pk, amt)
        user_detail = self.get_user_detail(pk)
        user_detail_serialized = UserDetailSerializer(user_detail)
        return Response(self.get_valid_message_body({
            "user_bank": user_detail_serialized.data
        }))


class UserHistoryAPI(FuzzyAPIView):
    def get(self, request):
        pk = request.query_params.get("pk", None)
        if not self.validate_input(pk):
            return Response(self.get_invalid_message())
        UserData = self.get_user(pk)
        UserDataSerialized = UserSerializer(UserData)
        UserHistoryData = self.get_user_history(pk)
        UserHistoryDataSerialized = UserHistorySerializer(
            UserHistoryData, many=True
        )
        return Response(self.get_valid_message_body({
            "user": UserDataSerialized.data,
            "user_history": UserHistoryDataSerialized.data
        }))

    def post(self, request):
        transaction_charge = request.data.get("transaction_charge", None)
        user_id = request.data.get("user_id", None)

        if not self.validate_input(transaction_charge, user_id):
            return Response(self.get_invalid_message())

        newUserHistoryUpdates = self.create_new_user_history(
            transaction_charge, user_id
        )

        if newUserHistoryUpdates == None or newUserHistoryUpdates == False:
            return Response(self.get_invalid_message())

        UserData = self.get_user(user_id)
        UserDataSerialized = UserSerializer(UserData)
        UserHistoryData = self.get_user_history(user_id)
        UserHistoryDataSerialized = UserHistorySerializer(
            UserHistoryData, many=True
        )
        return Response(self.get_valid_message_body({
            "user": UserDataSerialized.data,
            "user_history": UserHistoryDataSerialized.data
        }))


class ComparisonAPI(FuzzyAPIView):
    def post(self, request):
        sentence1 = request.data.get("sentences1", [])
        sentence2 = request.data.get("sentences2", [])
        comp_val = 0.0001

        if not self.validate_input(sentence1, sentence2):
            return Response(self.get_invalid_message())

        comp_val = MultiSentenceBertComparision(sentence1, sentence2)

        if len(sentence1) == len(sentence2):
            comp_val = [comp_val[i][i] for i in range(len(sentence1))]

        return Response(self.get_valid_message_body(comp_val))
