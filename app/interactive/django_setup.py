import os
import django


def start_django_in_notebook():
    os.environ["DJANGO_SETTINGS_MODULE"] = "wqdms.settings"
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
    django.setup()
