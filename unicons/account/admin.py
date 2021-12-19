from .models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import RegistrationForm, CustomUserAdminChangeForm, CustomUserAdminCreationForm


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserAdminChangeForm
    add_form = CustomUserAdminCreationForm

    list_display = ('email', 'name', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', )
    fieldsets = (
        (None, {"fields": ('email', 'is_staff', 'is_superuser', 'password'),}),
        ('Personal info', {'fields': ('name', )}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Personal info', {'fields': ('name', 'phone', 'date_of_birth', 'picture')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ('date_joined', 'last_login')


admin.site.register(CustomUser, CustomUserAdmin)
    
