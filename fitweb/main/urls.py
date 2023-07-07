from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name="home"),
    
    path("about/", views.about, name="about"),
    path("contact/", views.contact.as_view(), name="contact"),
    path("bmi/", views.bmi, name="bmi"),
    path("blog/", views.blog, name="blog"),
    path("diet/", views.diet, name="diet"),
    path("workout/", views.workout, name="workout"),
    path("portfolio/", views.portfolio, name="portfolio"),
]
