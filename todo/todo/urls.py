from django.urls import path
from . import views

# urls

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo_list'),
    path('todo_detail/<int:pk>/', views.TodoDetail.as_view(), name='todo_detail'),
    path('todo_update/<int:pk>/', views.TodoUpdate.as_view(), name='todo_update'),
    path('todo_delete/<int:pk>/', views.TodoDelete.as_view(), name='todo_delete'),
    path('todo_create/', views.TodoCreate.as_view(), name='todo_create'),
]
