from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ComputerScience100Level, InfoCenter, ComputerScience200Level, GeneralInfo, ComputerScience300Level, ComputerScience400Level
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.


class CustomUserAdmin(UserAdmin, admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active", )
    list_filter = ("email", "is_staff", "is_active", )
    fieldsets = (
        (None, {"fields": ("email", "password", "profile_image")}),
        ("permissions", {"fields": ("is_staff", "is_active","groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password", "level", "department", "is_staff", "is_active", "groups", "user_permissions"
            )
        }),
    )

    search_fields = ("email", )
    ordering = ("email",)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.set_password(obj.email)
        super().save_model(request, obj, form, change)


class ComputerScience100LevelAdmin(admin.ModelAdmin):
    readonly_fields = ['average_score', 'gpa']



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ComputerScience100Level, ComputerScience100LevelAdmin)
admin.site.register(ComputerScience200Level)
admin.site.register(ComputerScience300Level)
admin.site.register(ComputerScience400Level)
admin.site.register(InfoCenter)
admin.site.register(GeneralInfo)