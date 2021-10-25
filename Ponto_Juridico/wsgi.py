"""
WSGI config for Ponto_Juridico project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior
# ponto_juridico directory.
app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, 'ponto_juridico'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ponto_Juridico.settings')

application = get_wsgi_application()
