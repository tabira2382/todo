import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo.settings")

<<<<<<< HEAD
application = Cling(get_wsgi_application())
=======
application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
>>>>>>> 8e6135ba56e66da805befdb1cd9bb294ea1f1bc0
