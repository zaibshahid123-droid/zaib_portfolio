from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("projects/", views.ProjectListView.as_view(), name="project_list"),
    path("projects/<int:pk>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("blog/", views.BlogListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
