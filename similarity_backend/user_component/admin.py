from django.contrib import admin

from user_component.models import (
    User ,UserHistory, UserDetail, SemanticModel, QueryModel
)

admin.site.register(UserHistory)
admin.site.register(UserDetail)
admin.site.register(SemanticModel)
admin.site.register(QueryModel)
