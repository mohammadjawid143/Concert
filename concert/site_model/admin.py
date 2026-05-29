from django.contrib import admin
from site_model.models import site_setting
from site_model.models import ContactMessage
# Register your models here.
admin.site.register(site_setting)
admin.site.register(ContactMessage)

