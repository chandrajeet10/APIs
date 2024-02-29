from django.urls import path
from .views import *

urlpatterns = [
   path('<int:pk>/' , DetailToDo.as_view()),
   path('' , ListToDo.as_view()),
   path('' , createToDo.as_view()),
   path('delete/<int:pk>' , deleteToDo.as_view())

]