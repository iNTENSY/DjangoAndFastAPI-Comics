from django.contrib import admin
from django.contrib.auth import get_user_model


Users = get_user_model()


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
