from django.conf.urls import url

from story import views

urlpatterns = [
    # Register a new user
    url(r'^api/users', views.RegistrationView.as_view()),
]