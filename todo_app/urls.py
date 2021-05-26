from django.urls import path, include
from . import views

app_name = 'todo_app'

urlpatterns = [
    # path('', views.home, name='home'),
    # path('details/<int:id>', views.details, name="details"),
    # path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('', views.TaskListView.as_view(), name='home'),
    path('details/<int:pk>', views.TaskDetailView.as_view(), name='details'),
    path('update/<int:pk>', views.TaskUpdateView.as_view(), name='update'),
    path('add', views.add_new_todo, name='add')
]