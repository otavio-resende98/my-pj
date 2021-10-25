from django.apps import AppConfig


class MemberConfig(AppConfig):
    name = 'member'
    verbose_name = "Membro"

    def ready(self):
        import member.signals  # noqa
