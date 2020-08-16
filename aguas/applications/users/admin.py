from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'password',
        'email',
        'name',
        'last_name',
        'gender'
    )
admin.site.register(User,UserAdmin)