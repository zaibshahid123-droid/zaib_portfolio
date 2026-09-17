from django.core.management.base import BaseCommand
from portfolio.models import Skill, Project, BlogPost


SKILLS = [
    ("Python", "language", 90),
    ("Django", "framework", 90),
    ("JavaScript", "language", 75),
    ("REST APIs", "framework", 85),
    ("PostgreSQL", "database", 80),
    ("Git", "tool", 85),
    ("GitHub", "tool", 85),
    ("HTML", "language", 90),
    ("CSS", "language", 80),
    ("Bootstrap", "framework", 75),
    ("CI/CD", "tool", 65),
    ("Docker", "tool", 65),
]


class Command(BaseCommand):
    help = "Seed the portfolio app with starter skills, a sample project and blog post."

    def handle(self, *args, **options):
        for i, (name, category, proficiency) in enumerate(SKILLS):
            Skill.objects.update_or_create(
                name=name,
                defaults={"category": category, "proficiency": proficiency, "order": i},
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(SKILLS)} skills."))

        project, created = Project.objects.get_or_create(
            title="Django E-commerce Platform",
            defaults={
                "description": (
                    "A full-featured e-commerce app built with Django, practicing a "
                    "separated frontend/backend architecture and CORS configuration."
                ),
                "tech_stack": "Django, PostgreSQL, REST APIs, Bootstrap",
                "live_demo_url": "https://ecommerce-project-m9fsl9rxb-zaib4.vercel.app/",
                "featured": True,
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Seeded 1 sample project."))

        post, created = BlogPost.objects.get_or_create(
            title="Why I Chose Django for My Portfolio",
            defaults={
                "summary": "A quick look at why Django was the right fit for this site.",
                "content": (
                    "Django gives me a batteries-included framework — an admin panel, "
                    "ORM and forms out of the box — which makes it easy to manage "
                    "projects, blog posts and my resume without hard-coding content "
                    "into templates."
                ),
            },
        )
        if created:
            self.stdout.write(self.style.SUCCESS("Seeded 1 sample blog post."))
