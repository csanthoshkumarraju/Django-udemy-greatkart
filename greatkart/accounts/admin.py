from django.contrib import admin
from .models import Account,UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ['username','email','phone_number','last_login','is_active']
    list_filter = ['username','last_login','date_joined']
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# class UserProfileAdmin(UserAdmin):
#     # def thumbnail(self, object):
#     #     return format_html('<img src="{}" class="rounded-circle shadow-4" style="width: 60px;" alt="Avatar" />', object.profile_picture.url)
#     # thumbnail.short_description = 'profile_picture'

#     list_display = ['country', 'state', 'city']
#     list_filter = ['country', 'state']

    
    

admin.site.register(Account,AccountAdmin)
admin.site.register(UserProfile)