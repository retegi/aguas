from django.contrib import admin
from .models import StreetMap
from .models import Contact
from .models import Address
from .models import CommunityAgency

class CommunityAgencyAdmin(admin.ModelAdmin):
    list_display=(
        'name_CA',
        'address_CA',
        'phone1_CA',
        'phone2_CA',
        'email_CA',
        'info_CA',
    )
admin.site.register(CommunityAgency,CommunityAgencyAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'street_Address',
        'number_Address',
    )
admin.site.register(Address,AddressAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=(
        'name_contact',
        'lastname_contact',
        'phone1_contact',
        'phone2_contact',
        'email_contact',
        'detail_contact',
    )
admin.site.register(Contact,ContactAdmin)

class StreetMapAdmin(admin.ModelAdmin):
    list_display=(
        'name',
    )
admin.site.register(StreetMap,StreetMapAdmin)

