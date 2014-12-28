"""
WSGI config for ticketus project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketus.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
