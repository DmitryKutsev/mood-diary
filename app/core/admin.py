from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name',)}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        ('Important dates', {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Patient)
admin.site.register(models.Therapist)
admin.site.register(models.Diary)
admin.site.register(models.DiaryEntry)
admin.site.register(models.Mood)
admin.site.register(models.Emotion)
admin.site.register(models.Therapy)
admin.site.register(models.Supervision)
admin.site.register(models.Supervisor)
admin.site.register(models.Lvl)
