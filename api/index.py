import os
import sys

# Add project root directory to sys.path first
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings")

# Run collectstatic so WhiteNoise has the latest static files
try:
    from django.core.management import call_command
    call_command("collectstatic", "--noinput", "--clear")
except Exception as e:
    print(f"Error running collectstatic: {e}")

# Import WSGI application (importing 'application' and assigning to 'app')
from portfolio_site.wsgi import application

app = application