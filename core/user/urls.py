from django.urls import path
from core.user.views import *

urlpatterns = [
    # user
    path('', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('choose/profile/<int:pk>/', UserChooseGroup.as_view(), name='user_choose_profile'),
    path('update/profile/', UserUpdateProfileView.as_view(), name='user_update_profile'),
    path('change/password/', UserChangePasswordView.as_view(), name='user_change_password'),
]
