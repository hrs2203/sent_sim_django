from django.test import TestCase

from comparision_engine import MultiSentenceBertComparision


lb = MultiSentenceBertComparision( ["Death bed"], ["Nice time","good time","Nice day","grave yard"])


for i in zip(lb[0]):
    print(i)


