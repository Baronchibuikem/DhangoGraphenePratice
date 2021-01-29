from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from accounts.models import CustomUser, Role


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',  'is_active', 'email', 'user_id', 
                    "first_name", 'last_name',)

admin.site.register(Role)
