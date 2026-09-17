from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, TemplateView

from .models import Project, Skill, BlogPost, Resume
from .forms import ContactForm


class HomeView(ListView):
    """Home page: Hero + About + Skills + featured Projects + Contact form."""

    model = Project
    template_name = "portfolio/home.html"
    context_object_name = "projects"

    def get_queryset(self):
        qs = Project.objects.all()
        if qs.filter(featured=True).exists():
            qs = qs.filter(featured=True)
        return qs[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = Skill.objects.all()
        context["latest_posts"] = BlogPost.objects.filter(published=True)[:3]
        context["contact_form"] = ContactForm()
        return context


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"
    paginate_by = 9


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"


class BlogListView(ListView):
    model = BlogPost
    template_name = "portfolio/blog_list.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "portfolio/blog_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)


class ResumeView(TemplateView):
    template_name = "portfolio/resume.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resume"] = Resume.objects.filter(is_active=True).first()
        context["skills"] = Skill.objects.all()
        return context


class ContactView(FormView):
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("portfolio:contact")

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        subject = form.cleaned_data["subject"]
        message = form.cleaned_data["message"]

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject=f"[Portfolio Contact] {subject}",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
            fail_silently=False,
        )
        messages.success(self.request, "Thanks for reaching out! I'll get back to you soon.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please fix the errors below and try again.")
        return super().form_invalid(form)
