from django.urls import path, re_path

from suggestion import views

urlpatterns = [
    path('create', views.suggestion_all, name='create'),
    path('list', views.suggestion_all, name='list'),
    path('read/<int:id>', views.suggestion_by_id),
    path('update/<int:id>', views.suggestion_by_id),
    path('delete/<int:id>', views.suggestion_by_id),
]