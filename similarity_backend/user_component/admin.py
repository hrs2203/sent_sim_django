from django.contrib import admin

from user_component.models import (
    User ,UserHistory, UserDetail, QueryModel, HistorySentence
)

admin.site.register(UserHistory)
admin.site.register(UserDetail)
admin.site.register(QueryModel)
admin.site.register(HistorySentence)

