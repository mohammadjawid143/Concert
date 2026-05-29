from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ticketSales.urls')),
    path('accounts/', include('accounts.urls')),
    path('order_module/', include('order_module.urls')),
    path('site_model/', include('site_model.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
