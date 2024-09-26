from django.apps import AppConfig


class MaestrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.maestros'

    def ready(self):
        import apps.maestros.models.base_gen_models
        import apps.maestros.models.base_models
        