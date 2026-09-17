from django.conf import settings


def site_meta(request):
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_TAGLINE": settings.SITE_TAGLINE,
        "GITHUB_URL": settings.GITHUB_URL,
        "EMAIL_CONTACT": settings.EMAIL_CONTACT,
        # Placeholders — fill these in once you create the accounts.
        "LINKEDIN_URL": "",
        "TWITTER_URL": "",
        "INSTAGRAM_URL": "",
        "FACEBOOK_URL": "",
    }
