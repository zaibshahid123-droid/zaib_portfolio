from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    tech_stack = models.CharField(
        max_length=300,
        help_text="Comma separated, e.g. Django, PostgreSQL, Tailwind CSS",
    )
    github_url = models.URLField(blank=True)
    live_demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", kwargs={"pk": self.pk})

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Language"),
        ("framework", "Framework / Library"),
        ("database", "Database"),
        ("tool", "Tool / DevOps"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="tool")
    proficiency = models.PositiveSmallIntegerField(
        default=80, help_text="0-100, used for the skill bar width"
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    summary = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("portfolio:blog_detail", kwargs={"slug": self.slug})


class Resume(models.Model):
    """Keep just one active resume file/version."""

    title = models.CharField(max_length=150, default="My Resume")
    file = models.FileField(upload_to="resume/")
    summary = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
