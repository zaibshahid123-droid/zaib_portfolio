import os
import sys

# Add project root directory to sys.path first
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

# Import WSGI application after paths and settings are configured
from portfolio_site.wsgi import app