from rest_framework import viewsets
from .serialzer import TaskSerializer
from .models import Task

# Create your views here.


class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
