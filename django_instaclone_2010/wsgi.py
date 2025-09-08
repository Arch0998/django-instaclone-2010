import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv


load_dotenv()


settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", "settings.dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
