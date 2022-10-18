from django.urls import path
from core.security.views.access_users.views import *

urlpatterns = [
    path('access/users/', AccessUsersListView.as_view(), name='access_users_list'),
    path('access/users/delete/<int:pk>/', AccessUsersDeleteView.as_view(), name='access_users_delete'),
]
