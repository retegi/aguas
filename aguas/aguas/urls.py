from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('login/', include('applications.home.urls')),
    re_path('station/', include('applications.station.urls')),
    re_path('installation/', include('applications.installation.urls')),
    re_path('device/', include('applications.device.urls')),
    re_path('consumable/', include('applications.consumable.urls')),
    re_path('incidence/', include('applications.incidence.urls')),
    re_path('repair/', include('applications.repair.urls')),
    re_path('map/', include('applications.map.urls')),
    re_path('preventive/', include('applications.preventive.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
