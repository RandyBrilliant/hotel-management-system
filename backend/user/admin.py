from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserProfileInline(admin.StackedInline):
    model = Profile
    fk_name = 'user'


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    readonly_fields = ['date_joined', 'last_login']
    list_display = ['email', 'username', 'admin', 'last_login']
    list_filter = ['admin']
    fieldsets = (
        ('Credentials', {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('admin', 'staff')}),
        ('Activities', {'fields': ('date_joined', 'last_login')}),
    )
    inlines = [
        UserProfileInline,
    ]

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', 'password_2')}
         ),
    )
    search_fields = ['email', 'username']
    ordering = ['email', 'username']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
