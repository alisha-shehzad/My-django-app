from django.urls import path
from .views import (
    # Employee Views
    employee_list,
    get_employee,
    create_employee,
    update_employee,
    delete_employee,

    # User Views
    user_list,
    user_detail,
    create_user,
    update_user,
    delete_user
)

urlpatterns = [
    # Employee routes
    path('employees/', employee_list, name='employee-list'),
    path('employees/<int:pk>/', get_employee, name='employee-detail'),
    path('employees/create/', create_employee, name='employee-create'),
    path('employees/<int:pk>/update/', update_employee, name='employee-update'),
    path('employees/<int:pk>/delete/', delete_employee, name='employee-delete'),

    # User routes
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('users/create/', create_user, name='user-create'),
    path('users/<int:pk>/update/', update_user, name='user-update'),
    path('users/<int:pk>/delete/', delete_user, name='user-delete'),
]
