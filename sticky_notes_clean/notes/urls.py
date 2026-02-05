from django.urls import path
from . import views

# URLs for CRUD functions

urlpatterns = [
    # URL pattern for displaying list of all notes for user
    path('', views.note_list, name='note_list'),
    # URL pattern for displaying a specific note
    path('<int:pk>/', views.note_detail, name='note_detail'),
    # URL pattern for creating a note
    path('create/', views.note_create, name='note_create'),
    # URL pattern for updating a note
    path('<int:pk>/edit/', views.note_update, name='note_update'),
    # URL pattern for deleting a note
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
]
