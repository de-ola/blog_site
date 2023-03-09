from django.urls import path
from .views import *


urlpatterns = [
    path("", index.as_view(), name="index"),
    path("<int:pk>/", blogpost, name="blog_detail"),
    path("create/", create.as_view(), name="create"),
    #path("about_us/", dev_team.as_view(), name="dev_team"),
    path("edit/<int:pk>/", update.as_view(), name="update"),
    path("<int:pk>/delete/", delete.as_view(), name="delete"),
]