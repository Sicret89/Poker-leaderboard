from django.urls import include, path

from .views import upload_file_view

urlpatterns = [
    path("csv", upload_file_view, name="upload-view"),
]
