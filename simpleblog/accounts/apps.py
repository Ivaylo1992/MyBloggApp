from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "simpleblog.accounts"

    def ready(self):
        from simpleblog.accounts import signals
