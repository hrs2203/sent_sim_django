from user_component.models import User, UserHistory
from user_component.serializers import UserSerializer, UserHistorySerializer
from user_component.utils import SAMPLE

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user_component.comparision_engine import MultiSentenceBertComparision, CorpusBasedComparision


class FuzzyAPIView(APIView):
    """User class default api view providing default functions as needed"""

    INVALID_VALUE = "invalid input"
    DEFAULT_CHARGE = 10

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
        """ create unique user by email ? if present, returns from db"""
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
        """ Get user history by user id """
        data = []
        try:
            data = UserHistory.objects.filter(user_id=pk)
        except:
            pass
        return data

    def create_new_user_history(
        self,
        model_utilized: str,
        transaction_charge: str,
        user_id: int
    ):
        user_obj = self.get_user(user_id)
        if user_obj == None:
            return None
        newUserHistory = UserHistory(
            model_utilized=model_utilized,
            transaction_charge=transaction_charge,
            user_id=user_obj
        )
        try:
            newUserHistory.save()
        except:
            pass
        return newUserHistory

    def get_transaction_charge(self):
        return self.DEFAULT_CHARGE

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


class UserHistoryAPI(FuzzyAPIView):
    def get(self, request):
        pk = request.data.get('pk', None)

        if not self.validate_input(pk):
            return Response(self.get_invalid_message())

        UserHistoryData = self.get_user_history(pk)
        UserHistoryDataSerialized = UserHistorySerializer(
            UserHistoryData, many=True)
        return Response(self.get_valid_message_body(UserHistoryDataSerialized.data))

    def post(self, request):
        model_utilized = request.data.get("model_utilized", None)
        transaction_charge = request.data.get("transaction_charge", None)
        user_id = request.data.get("user_id", None)

        if not self.validate_input(model_utilized, transaction_charge, user_id):
            return Response(self.get_invalid_message())

        newUserHistory = self.create_new_user_history(
            model_utilized, transaction_charge, user_id)

        if newUserHistory == None:
            return Response(self.get_invalid_message())

        newUserHistorySerialized = UserHistorySerializer(newUserHistory)
        return Response(self.get_valid_message_body(newUserHistorySerialized.data))


class ComparisonAPI(FuzzyAPIView):

    ## TODO: Might have to create seprate api to comparision endpoints

    # TODO: Use this for corpus based comparision
    def pair_comparision(self, sent1: str, sent2: str):
        return CorpusBasedComparision(sent1, sent2)

    # TODO: Use this for SentBertComparision
    def multpile_pair_comp(self, sentence_list_1: list, sentence_list_2: list):
        return MultiSentenceBertComparision(sentence_list_1, sentence_list_2)

    def __init__(self):
        self.COMPARIONS_ENGINE = dict()
        self.COMPARIONS_ENGINE["CorpusBasedComparision"] = self.pair_comparision
        self.COMPARIONS_ENGINE["MultiSentenceBertComparision"] = self.multpile_pair_comp

    def sample_comp(self, sent1, sent2):
        """ Sample algo for show """
        return 0.0

    def post(self, request):
        algorithm = request.data.get("algorithm", None)
        sentence1 = request.data.get("sentence1", None)
        sentence2 = request.data.get("sentence2", None)
        comp_val = 0.0001

        if not self.validate_input(algorithm, sentence1, sentence2):
            return Response(self.get_invalid_message())

        if algorithm == "CorpusBasedComparision":
            comp_val = CorpusBasedComparision(sentence1, sentence2)
        elif algorithm == "MultiSentenceBertComparision":
            comp_val = MultiSentenceBertComparision([sentence1], [sentence2])[0][0]

        return Response(self.get_valid_message_body( comp_val ))
