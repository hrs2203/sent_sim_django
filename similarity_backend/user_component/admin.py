from django.contrib import admin

from user_component.models import (
    UserHistory, UserDetails, SemanticModel, QueryModel
)


admin.site.register(UserHistory)
admin.site.register(UserDetails)
admin.site.register(SemanticModel)
admin.site.register(QueryModel)
