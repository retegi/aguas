from django.contrib import admin
from .models import Company
from .models import Email
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'vat_company',
    )
admin.site.register(Company,CompanyAdmin)

class EmailAdmin(admin.ModelAdmin):
    list_display=(
        'address_email',
        'description_email',
    )
admin.site.register(Email,EmailAdmin)