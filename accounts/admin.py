from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for user management with add and change forms plus password
    """

    model = User
    list_display = ("id","email", "is_superuser", "is_active", "is_verified","type")
    list_filter = ("email", "is_superuser", "is_active", "is_verified","type")
    searching_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions","type"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                    "type",
                ),
            },
        ),
    )

class CustomProfileAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name",)

admin.site.register(Profile,CustomProfileAdmin)
admin.site.register(User, CustomUserAdmin)
