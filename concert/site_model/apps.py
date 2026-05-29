from django.apps import AppConfig


class SiteModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_model'
    verbose_name='Site Settings'