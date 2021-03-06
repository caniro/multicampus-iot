from django.forms.models import ALL_FIELDS
from django.urls import path
from bookmark.views import *

app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='index'),
    path('<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('add/', BookmarkCreateView.as_view(), name="add"),
    path('change/', BookmarkChangeListView.as_view(), name="change"),
    path('<int:pk>/update/', BookmarkUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(), name="delete"),
]
