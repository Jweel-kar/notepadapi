from django.urls import path

from . import views

urlpatterns = [
  path('notepads/', views.NotepadView.as_view()),
  path('notepads/<int:id>/', views.NotepadView.as_view()),
]