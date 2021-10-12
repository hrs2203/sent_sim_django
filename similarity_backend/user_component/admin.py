from django.contrib import admin

from user_component.models import (
    User ,UserHistory, UserDetail, QueryModel
)

admin.site.register(UserHistory)
admin.site.register(UserDetail)
admin.site.register(QueryModel)
