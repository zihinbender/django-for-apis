from django.urls import path

from .models import Todo
from .views import TodoDetail, TodoList

urlpatterns = [
    path("<int:pk>", TodoDetail.as_view(), name="todo_detail"),
    path("", TodoList.as_view(), name="todo_list"),
]