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

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password) 
        super().save_model(request, obj, form, change)

admin.site.register(User,UserAdmin)