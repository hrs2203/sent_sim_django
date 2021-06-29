from django.contrib.auth import authenticate
from rest_framework.fields import USE_READONLYFIELD

from .models import User, UserHistory
from .serializers import UserSerializer, UserHistorySerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserAPIView(APIView):
    """User class default api view providing default functions as needed"""

    INVALID_VALUE = {
        "message": "invalid input"
    }

    def get_all_user(self):
        return User.objects.all()

    def get_user(self, pk: int):
        data = None
        try:
            data = User.objects.get(pk=pk)
        except:
            data = None
        return data

    def get_user_email(self, email: str):
        data = None
        try:
            data = User.objects.get(email=email)
        except:
            data = None
        return data

    def create_new_user(self, username: str, email: str, password: str):
        check_user = self.get_user_email(email)
        if check_user == None:
            newUser = User.objects.create_user(username, email, password)
            try:
                newUser.save()
            except:
                pass
            return newUser
        return check_user

    def get_user_history(self, pk: int):
        data = None
        try:
            data = UserHistory.objects.get(pk=pk)
        except:
            pass
        return data

    def create_new_user_history(
        self,
        model_utilized: str,
        transaction_charge: str,
        user_id: int
    ):
        newUserHistory = UserHistory(
            model_utilized=model_utilized,
            transaction_charge=transaction_charge,
            user_id=user_id
        )
        try:
            newUserHistory.save()
        except:
            pass
        return newUserHistory

    def get_transaction_charge(self):
        return 10

    def get_invalid_message(self, msg=None):
        msg = msg or "invalid input"
        return {"statue": 400, "data": msg}

    def get_valid_message_body(self, body=None):
        body = body or {}
        return {"statue": 200, "data": body}

    def validate_input(self, *args):
        "Validate that no entry is false"
        for item in args:
            if item == None:
                return False
        return True


class LoginUser(UserAPIView):
    def post(self, request):

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not self.validate_input(email, password):
            return Response(self.get_invalid_message())

        user_object = self.get_user_email(email=email)
        if user_object == None:
            return Response(self.get_invalid_message(self.INVALID_VALUE["message"]))
        if not user_object.check_password(password):
            return Response(self.get_invalid_message("Invalid Password"))
        UserSerialized = UserSerializer(user_object)
        return Response(self.get_valid_message_body(UserSerialized.data))


class RegisterUser(UserAPIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        username = request.data.get('username', None)

        if not self.validate_input(email, password, username):
            return Response(self.get_invalid_message())

        newuser = self.create_new_user( username, email, password )
        UserSerialized = UserSerializer(newuser)
        return Response(self.get_valid_message_body(UserSerialized.data))
