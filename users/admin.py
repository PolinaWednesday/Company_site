from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка пользователей"""
    exclude = ('password',)