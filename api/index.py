"""
Vercel serverless entry point.

Vercel's Python runtime looks for a WSGI-compatible `app` (or `handler`)
object in this file. We just hand it Django's WSGI application.
"""
from portfolio_site.wsgi import app

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402

app = get_wsgi_application()
