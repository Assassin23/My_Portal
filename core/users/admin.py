from django.contrib import admin
from core.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    list_filter = ['email', 'first_name']
    search_fields = ['email', 'first_name', 'last_name']
    fields = ['email', 'first_name', 'last_name', 'address', 'zip_code', 'state', 'city']
