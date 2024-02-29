from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class DetailToDo(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class createToDo(generics.CreateAPIView):   
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class deleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer    