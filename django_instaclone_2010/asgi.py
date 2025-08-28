import os
from django.core.asgi import get_asgi_application
from dotenv import load_dotenv


load_dotenv()


settings_module = os.environ.get("DJANGO_SETTINGS_MODULE", "settings.dev")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_asgi_application()
