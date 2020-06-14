from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('add-todo', views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo')

]
