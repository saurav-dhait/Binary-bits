from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):
    list_display = ["agency_id"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2",
                           "first_name", "last_name", "email",
                           "is_active", "is_staff", "is_superuser",
                           "groups", "user_permissions", "agency_id"),
            },
        ),
    )


admin.site.register(MyUser, UserAdmin)
