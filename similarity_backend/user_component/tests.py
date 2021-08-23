from django.test import TestCase

from comparision_engine import MultiSentenceBertComparision, CorpusBasedComparision

print(
    CorpusBasedComparision("Nice Day","Nice time"),
    CorpusBasedComparision("Nice Day","good time"),
    CorpusBasedComparision("Nice Day","Nice Day"),
    CorpusBasedComparision("Nice Day","bad dog")
)

print(
    MultiSentenceBertComparision(
        ["Nice day"], ["Nice time","good time","Nice day","bad dog"]
    )
)