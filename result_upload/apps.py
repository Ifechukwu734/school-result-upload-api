from django.apps import AppConfig


class ResultUploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'result_upload'

    def ready(self):
        from . import signals
