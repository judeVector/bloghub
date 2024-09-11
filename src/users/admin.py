from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea
from .models import NewUser


# Register your models here.
class UserAdminConfig(UserAdmin):

    model = NewUser
    list_filter = ["email", "user_name", "first_name", "is_active", "is_staff"]
    search_fields = ["email", "user_name", "first_name"]
    ordering = [
        "-date_joined",
    ]
    list_display = ["email", "id", "user_name", "first_name", "is_active", "is_staff"]
    fieldsets = [
        [
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                ),
            },
        ],
        ["Permissions", {"fields": ["is_staff", "is_active"]}],
        [
            "Personal",
            {
                "fields": [
                    "about",
                ]
            },
        ],
    ]
    formfield_overrides = {
        NewUser.about: {"widget": Textarea(attrs={"rows": 10, "cols": 40})}
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "about",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(NewUser, UserAdminConfig)
