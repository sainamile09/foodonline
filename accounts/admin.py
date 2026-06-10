from django.contrib import admin
from . import models
from django.contrib.auth.admin  import UserAdmin

# Register your models here.

class CustomerUserAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_name','joined_date','is_active','is_staff')
    ordering = ('-joined_date',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(models.User,CustomerUserAdmin)
admin.site.register(models.UserProfile)
