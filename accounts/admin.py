from django.contrib import admin
from . import models
from django.contrib.auth.admin  import UserAdmin

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_name','joined_date','is_active','is_staff')
    ordering = ('-joined_date',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ('Personal Info', {'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password')}),
        ('Role', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superadmin')}),
        ('Important Dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number', 'role', 'password1', 'password2'),
        }),
    )

class UserProfileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('profile_picture') == False:
            obj.profile_picture = None
        if form.cleaned_data.get('cover_picture') == False:
            obj.cover_picture = None
        super().save_model(request, obj, form, change)

admin.site.register(models.User,CustomerUserAdmin)
admin.site.register(models.UserProfile, UserProfileAdmin)
