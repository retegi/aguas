from django.contrib import admin
from .models import Home
from .models import SocialMedia

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'contact_email',
        'web_address',
        'image_file_name'
    )
admin.site.register(Home,HomeAdmin)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        'name_social_network',
        'address_social_network',
    )
admin.site.register(SocialMedia,SocialMediaAdmin)