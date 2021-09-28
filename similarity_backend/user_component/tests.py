from django.test import TestCase

from comparision_engine import MultiSentenceBertComparision, CorpusBasedComparision

la = [
    CorpusBasedComparision("Death bed","Nice time"),
    CorpusBasedComparision("Death bed","good time"),
    CorpusBasedComparision("Death bed","Nice Day"),
    CorpusBasedComparision("Death bed","grave yard")
]

lb = MultiSentenceBertComparision( ["Death bed"], ["Nice time","good time","Nice day","grave yard"])


for i in zip(la, lb[0]):
    print(i)


