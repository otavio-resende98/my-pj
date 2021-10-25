from django.apps import AppConfig


class ActivityConfig(AppConfig):
    name = 'activity'
    verbose_name = "Atividade"

    def ready(self):
        import activity.signals  # noqa
