from django.urls import path

from . import views

# define namespace
app_name = "hello"
# using django generic views
urlpatterns = [
    # ex: /hello/
    path("", views.myview, name="index"),
]
