from rest_framework import generics, serializers
from .models import Todos
from .serializers import TodoSerializer

class ListTodo(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodoSerializer
