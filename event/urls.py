from django.urls import path, re_path
from event import views

urlpatterns = [
    path('create', views.event_all, name='create'),
    path('list', views.event_all, name='list'),
    # re_path(r'^detail/(?P<pk>[0-9]+)$', views.event_detail),
    path('read/<int:id>', views.event_by_id),
    path('update/<int:id>', views.event_by_id),
    path('completion/<int:id>', views.event_by_id),
    path('delete/<int:id>', views.event_by_id),
    path('date/<date>', views.event_by_time),
    path('title/<title>', views.event_by_title),
    # path('patch/<int:id>', views.event_state),
    # re_path(r'list/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})$', views.event_by_time),
]