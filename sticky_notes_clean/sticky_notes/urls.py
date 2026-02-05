
from django.contrib import admin
from django.urls import path, include


# Define URL patterns for the project
urlpatterns = [
    # Admin mapping to Django admin interface
    path('admin/', admin.site.urls),
    # URL patterns from the notes app (specifying root directory)
    path('', include('notes.urls')),
]
